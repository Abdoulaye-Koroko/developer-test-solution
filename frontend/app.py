from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()

# Mount static files and templates directories
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Function to compute the odds that Millennium Falcon reaches Endor in time and saves the galaxy
def compute_odds(data):
    # Replace this function with your actual odd calculation logic based on the data
    # For demonstration purposes, we assume that the data contains a "success_rate" field
    # representing the probability of success in percentage
    success_rate = data.get("success_rate", 0)
    return success_rate


@app.get("/", response_class=HTMLResponse)
async def read_item():
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/calculate-odds/")
async def calculate_odds(file: UploadFile = File(...), function_code: str = Form(...)):
    try:
        data = await file.read()
        data_dict = json.loads(data)

        # Replace the function_name with the actual function name you want to use for calculating the odds
        function_name = "calculate_odd"  # This should match the name of the function you want to use

        # Get the function from the function_code provided by the user
        function = {}
        exec(function_code, function)
        odd_function = function.get(function_name)

        # Call the odd function with the data
        odds = odd_function(data_dict)

        return {"odds": odds}

    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail="Invalid JSON data in the file.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the file.")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
