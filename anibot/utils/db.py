import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticClient, AgnosticDatabase, AgnosticCollection
from .. import DB_URL

__all__ = ['get_collection']

# Async function to initialize the database
async def initialize_db():
    try:
        async with AsyncIOMotorClient(DB_URL) as client:
            if "anibot" in await client.list_database_names():
                print("anibot Database Found :) => Now Logging to it...")
            else:
                print("anibot Database Not Found :( => Creating New Database...")

            database = client["anibot"]
            # Your additional initialization code goes here

    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        # Handle the error as needed, maybe exit the script or log the error

# Run the async initialization function using asyncio.run
asyncio.run(initialize_db())

# Access the initialized database
_DATABASE: AgnosticDatabase = AsyncIOMotorClient(DB_URL)["anibot"]

# Function to get or create a collection
def get_collection(name: str) -> AgnosticCollection:
    return _DATABASE[name]

# Function to close the database connection
def close_db() -> None:
    AsyncIOMotorClient(DB_URL).close()
