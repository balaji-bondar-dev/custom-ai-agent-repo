import asyncio

#define the coroutine to fetch data
async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulate a network request
    print("Data fetched")
    return {"data": "Sample data"}

#define the main coroutine to run the program   
async def main():
    print("Main function started")
    data = await fetch_data()
    print(f"Received data: {data}") 
    await asyncio.sleep(1)
    print("Main function completed")

#asyncio.run(main()) 

#run the main coroutine and wait for it to complete
await main()
