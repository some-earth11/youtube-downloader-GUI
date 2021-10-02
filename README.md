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

## Screenshots
### Interface
![Youtube Downloader Python](https://github.com/some-earth11/youtube-downloader/blob/main/Images/ss1.jpg)
### Browse Function
![Youtube Downloader Python](https://github.com/some-earth11/youtube-downloader/blob/main/Images/ss2.jpg)
### Process
![Youtube Downloader Python](https://github.com/some-earth11/youtube-downloader/blob/main/Images/ss3.jpg)
### Video Downloaded Successfully
![Youtube Downloader Python](https://github.com/some-earth11/youtube-downloader/blob/main/Images/ss5.jpg)
### Destination Folder
![Youtube Downloader Python](https://github.com/some-earth11/youtube-downloader/blob/main/Images/ss6.jpg)
### Seems Fine :)
![Youtube Downloader Python](https://github.com/some-earth11/youtube-downloader/blob/main/Images/ss7.jpg)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
