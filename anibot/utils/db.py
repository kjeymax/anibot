import asyncio
from pyrogram import idle
from . import anibot, has_user, session
from .utils.db import _close_db

user = None
if has_user:
    from . import user

async def main():
    try:
        await anibot.start()
        if user is not None:
            await user.start()

        await idle()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        await anibot.stop()
        if user is not None:
            await user.stop()

        _close_db()
        await session.close()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
