# Youtube Downloader

This Python and Tkinter based GUI allows users to directly download the Best Resolution Videos and Audios from Youtube.

## Pa-fy Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pafy.
Pafy along with Youtube-dl should be installed.

```bash
pip install pafy
pip install youtube-dl
```

## Usage

```python
import pafy

url = input("Enter Video URL: ")
video = pafy.new(url) 

# Downloads the best resolution possible       
best = video.getbest()   
best.download()
```
For a more detailed usage guide  , check out [Pafy - Tutorial](https://www.geeksforgeeks.org/youtube-mediaaudio-download-using-python-pafy/) .

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)