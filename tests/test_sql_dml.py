#
# This source file is part of the EdgeDB open source project.
#
# Copyright 2016-present MagicStack Inc. and the EdgeDB authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


from edb.tools import test
from edb.testbase import server as tb

try:
    import asyncpg
    from asyncpg import serverversion
except ImportError:
    pass


class TestSQLDataModificationLanguage(tb.SQLQueryTestCase):

    def setUp(self):
        self.stran = self.scon.transaction()
        self.loop.run_until_complete(self.stran.start())
        super().setUp()

    def tearDown(self):
        try:
            self.loop.run_until_complete(self.stran.rollback())
        finally:
            super().tearDown()

    SETUP = [
        """
        create type User;

        create type Document {
          create property title: str {
            create rewrite insert using (.title ++ ' (new)');
            create rewrite update using (.title ++ ' (updated)');
          };
          create multi property keywords: str;

          create link owner: User {
            create property is_author: bool;
          };
          create multi link shared_with: User {
            create property can_edit: bool;
          };
        };
    """
    ]

    async def test_sql_dml_insert_01(self):
        # base case
        await self.scon.execute(
            '''
            INSERT INTO "Document" (title) VALUES ('Meeting report')
            '''
        )
        res = await self.squery_values('SELECT title FROM "Document"')
        self.assertEqual(res, [['Meeting report (new)']])

    async def test_sql_dml_insert_02(self):
        # when columns are not specified, all columns are expected,
        # in alphabetical order:
        # id, __type__, owner, title
        with self.assertRaisesRegex(
            asyncpg.UndefinedTableError,
            "cannot assign to link '__type__': it is protected",
        ):
            await self.scon.execute(
                '''
                INSERT INTO "Document" VALUES (NULL, NULL, NULL, 'Report')
                '''
            )
            res = await self.squery_values('SELECT title FROM "Document"')
            self.assertEqual(res, [['Report (new)']])

    async def test_sql_dml_insert_03(self):
        # multiple rows at once
        await self.scon.execute(
            '''
            INSERT INTO "Document" (title) VALUES ('Report'), ('Briefing')
            '''
        )
        res = await self.squery_values('SELECT title FROM "Document"')
        self.assert_data_shape(
            res, tb.bag([['Report (new)'], ['Briefing (new)']])
        )

    async def test_sql_dml_insert_04(self):
        # using arbitrary query instead of VALUES
        await self.scon.execute(
            '''
            INSERT INTO "Document" (title)
            SELECT c FROM (
                SELECT 'Report', 1 UNION ALL SELECT 'Briefing', 2
            ) t(c, x)
            WHERE x >= 2
            '''
        )
        res = await self.squery_values('SELECT title FROM "Document"')
        self.assert_data_shape(res, tb.bag([['Briefing (new)']]))

    async def test_sql_dml_insert_05(self):
        # insert link
        await self.scon.execute('INSERT INTO "User" DEFAULT VALUES;')
        await self.scon.execute(
            'INSERT INTO "Document" (owner_id) SELECT id FROM "User" LIMIT 1'
        )
        res = await self.squery_values('SELECT owner_id FROM "Document"')
        self.assert_shape(res, rows=1, columns=1)

    async def test_sql_dml_insert_06(self):
        # insert in a subquery: syntax error
        with self.assertRaisesRegex(
            asyncpg.PostgresSyntaxError, 'syntax error at or near "INTO"'
        ):
            await self.scon.execute(
                '''
                SELECT * FROM (
                    INSERT INTO "Document" (title) VALUES ('Meeting report')
                )
                '''
            )

    async def test_sql_dml_insert_07(self):
        # insert in a CTE
        await self.scon.execute(
            '''
            WITH a AS (
                INSERT INTO "Document" (title) VALUES ('Meeting report')
            )
            SELECT * FROM a
            '''
        )

    async def test_sql_dml_insert_08(self):
        # insert in a CTE: invalid PostgreSQL
        with self.assertRaisesRegex(
            asyncpg.FeatureNotSupportedError,
            'WITH clause containing a data-modifying statement must be at '
            'the top level',
        ):
            await self.scon.execute(
                '''
                WITH a AS (
                    WITH b AS (
                        INSERT INTO "Document" (title) VALUES ('Meeting report')
                    )
                    SELECT * FROM b
                )
                SELECT * FROM a
                '''
            )
