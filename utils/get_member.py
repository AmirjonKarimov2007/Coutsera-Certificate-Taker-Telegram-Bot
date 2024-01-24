from loader import db

async def main():
    users = await db.select_all_certificate_data_user()
    
    # Process the users as needed
    print('users')

# Run the asynchronous function

