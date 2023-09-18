# Photo sorting by face

This Python app allows you to automatically organize photos in a folder, based on the person in the photo, with face recognition technology.

ex:
- Desktop
    - photo1.png => in this photo there is a person
    - photo2.png => same person of photo1
    - photo3.png => different person from photo1
    - photo4.png => same person of photo3
    - photo5.png => another person
    
it creates sub-folders
- Desktop
    - person0 
        - photo1.png
        - photo2.png
    - person1
        - photo3.png
        - photo4.png
    - person2
        - photo5.png

## How it works

it works this way:
    - Highlight a folder from the GUI
    - then click select
    - the program scans through all the files and for every image it finds
    - creates a sub-folder for each person in the path you selected, and puts all the images in the correct folders based on face recognition

## Installation

Follow these steps to set up your local development environment:

1. Clone the repository:
    ```
    git clone https://github.com/giuseppetrovato20/photo-sorting-by-face.git
    ```

2. Navigate into the cloned project:
    ```
    cd photo-sorting-by-face
    ```

3. Create a new virtual environment using Python's `venv` module:
    ```
    python3 -m virtualenv photo-sorting-by-face-env
    ```

4. Activate the virtual environment:
    - On Windows, run: 
        ```
        .\venv\Scripts\activate
        ```
    - On Unix or MacOS, run: 
        ```
        source venv/bin/activate
        ```

5. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## How to run

run 
```
python main.py
```

Now, you should be able to run the project in your local development environment.


Contributions are welcome.
