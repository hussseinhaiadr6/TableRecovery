# TableRecovery README
This a Full pipeline to detecet Tables in PDF and extract them to excel format 
it uses table detection 
text detecetion 
text recognition
an dtavle strcuture recingintion algorithm
## Setup Instructions

### 1. Clone the Repository

#### 1.1 Create a folder "WhateverName" in your desired location. This will be referred to as `your_path`. It should look something like `C:/Users/.../WhateverName`.

#### 1.2 Clone the repository using the following command:

```sh
git clone https://github.com/hussseinhaiadr6/TableRecovery.git
```




### 2. Set Up Virtual Environment
#### 2.1 You may need to install virtualenv if you don't already have it. Run:
``` sh
Copy code
pip install virtualenv
```
#### 2.2 Ensure you have Python 3.9 installed. If not, download and install it from Python's official site.

#### 2.3 Create a virtual environment using the Python 3.9 executable. Replace your_path and your_env_name with your chosen names:
```sh
Copy code
virtualenv -p C:/Users/HHR6/AppData/Local/Programs/Python/Python39/python.exe C:/Users/.../WhateverName/your_env_name
```
### 3. Activate the Environment
#### 3.1 Navigate to the Scripts directory of your virtual environment and activate it:
```sh

cd C:/Users/.../WhateverName/your_env_name/Scripts
activate
```
### 4. Install Dependencies
#### 4.1 Change the directory to where the requirements.txt file is located:
```sh

cd C:/Users/.../WhateverName/TableRecovery
```
#### 4.2 Install the required packages:
```sh

pip install -r requirements.txt
```
### 5. Clone PaddleOCR Repository
#### 5.1 Navigate to the TableRecovery directory:
```sh

cd C:/Users/.../WhateverName/TableRecovery
```
#### 5.2 Clone the PaddleOCR repository:
``` sh

git clone https://github.com/PaddlePaddle/PaddleOCR.git
```
### 6. Configure the Pipeline
#### 6.1 Open the Pipline.py file and change the input_filename to the path of your PDF file. It should look something like:
```python

input_filename = "C:/Users/.../File.pdf"
```

### 7. Run the Pipeline
#### 7.1 Run the pipeline using the following command:
```sh

python Pipline.py
```
This should execute the pipeline and process your PDF file as needed.
