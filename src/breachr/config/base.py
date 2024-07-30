from __future__ import annotations


from dotenv import load_dotenv




load_dotenv()



class DatabaseConfig:
    
    DUCKDB_DATABASE: str = "data/duckdb.db"
    
    
    
    
class Settings:
        
    DEBUG: bool = True
    TESTING: bool = False
    DATABASE: DatabaseConfig = DatabaseConfig()