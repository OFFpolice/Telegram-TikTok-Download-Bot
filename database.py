import aiosqlite


async def database_initialization():
    async with aiosqlite.connect('data/main.db') as db:
        await db.execute('''CREATE TABLE IF NOT EXISTS main_table
                            (user_id INTEGER PRIMARY KEY, 
                             language TEXT, 
                             download_count INT DEFAULT 0)''')

        await db.execute('''CREATE TABLE IF NOT EXISTS downloads
                            (url TEXT PRIMARY KEY, 
                             file_id TEXT NOT NULL, 
                             caption TEXT)''')
        await db.commit()


async def get_user_language(user_id):
    async with aiosqlite.connect('data/main.db') as db:
        async with db.execute("SELECT language FROM main_table WHERE user_id = ?", (user_id,)) as cursor:
            result = await cursor.fetchone()
            return result[0] if result else None


async def set_user_language(user_id, language):
    async with aiosqlite.connect('data/main.db') as db:
        await db.execute('''INSERT OR REPLACE INTO main_table (user_id, language) 
                            VALUES (?, ?)''', (user_id, language))
        await db.commit()


async def new_user(user_id):
    async with aiosqlite.connect('data/main.db') as db:
        async with db.execute('SELECT * FROM main_table WHERE user_id = ?', (user_id,)) as cursor:
            if not await cursor.fetchone():
                await db.execute('INSERT INTO main_table (user_id) VALUES (?)', (user_id,))
                await db.commit()


async def get_users_count():
    async with aiosqlite.connect('data/main.db') as db:
        async with db.execute('SELECT COUNT(*) FROM main_table') as cursor:
            result = await cursor.fetchone()
            return result[0]


async def get_users():
    async with aiosqlite.connect('data/main.db') as db:
        async with db.execute('SELECT user_id FROM main_table') as cursor:
            result = await cursor.fetchall()
            return [user[0] for user in result]


async def add_new_download(url, file_id, caption):
    async with aiosqlite.connect('data/main.db') as db:
        await db.execute('''INSERT OR REPLACE INTO downloads (url, file_id, caption) 
                            VALUES (?, ?, ?)''', (url, file_id, caption))
        await db.commit()


async def get_saved_video(url):
    async with aiosqlite.connect('data/main.db') as db:
        async with db.execute('SELECT file_id, caption FROM downloads WHERE url = ?', (url,)) as cursor:
            result = await cursor.fetchone()
            return {"file_id": result[0], "caption": result[1]} if result else None


async def add_new_download_count():
    async with aiosqlite.connect('data/main.db') as db:
        async with db.execute('SELECT download_count FROM main_table') as cursor:
            current_count = await cursor.fetchone()
            if current_count is not None:
                new_count = current_count[0] + 1
                await db.execute('UPDATE main_table SET download_count = ?', (new_count,))
            else:
                await db.execute('INSERT INTO main_table (download_count) VALUES (1)')
        await db.commit()


async def get_downloads():
    async with aiosqlite.connect('data/main.db') as db:
        async with db.execute('SELECT download_count FROM main_table') as cursor:
            result = await cursor.fetchone()
            return result[0] if result else 0
