# main.py
import os
import re
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import List, Any
from dotenv import load_dotenv

load_dotenv()  # loads .env if present

FULL_NAME = os.getenv("FULL_NAME", "john_doe")
DOB = os.getenv("DOB_DDMMYYYY", "17091999")
EMAIL = os.getenv("EMAIL", "john@xyz.com")
ROLL_NUMBER = os.getenv("ROLL_NUMBER", "ABCD123")

app = FastAPI(title="BFHL API")

digits_re = re.compile(r'^\d+$')
alpha_re = re.compile(r'^[A-Za-z]+$')

class DataRequest(BaseModel):
    data: List[Any]

@app.post("/bfhl")
async def bfhl(req: DataRequest):
    try:
        input_array = req.data

        even_numbers: List[str] = []
        odd_numbers: List[str] = []
        alphabets: List[str] = []
        special_characters: List[str] = []
        sum_int = 0
        letters_sequence: List[str] = []  # single characters in order

        for item in input_array:
            s = str(item).strip()

            if s == "":
                # treat empty string as special character
                special_characters.append(s)
                continue

            if digits_re.match(s):
                n = int(s)
                if n % 2 == 0:
                    even_numbers.append(s)  # keep as string
                else:
                    odd_numbers.append(s)
                sum_int += n
            elif alpha_re.match(s):
                alphabets.append(s.upper())  # token -> uppercase
                for ch in s:  # collect characters in original order
                    letters_sequence.append(ch)
            else:
                special_characters.append(s)

        # Build concat_string: reverse letters_sequence, then alternating caps (start UPPER)
        reversed_seq = list(reversed(letters_sequence))
        concat_chars = [
            (ch.upper() if i % 2 == 0 else ch.lower())
            for i, ch in enumerate(reversed_seq)
        ]
        concat_string = "".join(concat_chars)

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(sum_int),
            "concat_string": concat_string
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail={"is_success": False, "error": str(e)})
