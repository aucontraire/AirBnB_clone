# AirBnB Clone

## Description

This is the first of several lite clones of the [AirBnB](https://www.airbnb.com) (online platform for rental accommodations) website. It specifies classes for __User__, __Place__, __State__, __City__, __Amenity__, and __Review__ that inherit from the __BaseModel__ class. Instances are serialized and saved to a JSON file then reloaded and deserialized back into instances. Additionally, there is a simple command line interface (CLI) or 'console' that abstracts the process used to create these instances.

## Usage

The console can run in two modes: *interactive* and *non-interactive*:

### Interactive mode

To run the console in *interactive* mode type:

```$ ./console.py```

This prompt will appear:

```(hbnb) ```

where you can type commands and get output. For example:

```(hbnb) all```

```[[User] (0a7adbf6-ea6f-4447-9e7e-c160687632e7) {'id': '0a7adbf6-ea6f-4447-9e7e-c160687632e7', 'updated_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906), 'created_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906)}]```

### Non-interactive mode

The same commands can be used to run non-interactive mode with some modifications:

```$ echo "all" | ./console.py ```

will produce the same results as above:

```[[User] (0a7adbf6-ea6f-4447-9e7e-c160687632e7) {'id': '0a7adbf6-ea6f-4447-9e7e-c160687632e7', 'updated_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906), 'created_at': datetime.datetime(2018, 6, 13, 23, 38, 38, 231906)}]```

You can also use a file that contains the commands you want to run:

```$ cat commands.txt | ./console.py```

### Storage

Instances of classes are saved in a [JSON](https://www.json.org) string representation to the __file.json__ file at the root directory. Any modifications (additions, deletions, updates) to the objects are saved automatically to the file. The JSON file serves as a simple database that helps the data persist across sessions. 


### Tests
Testing is imperative to building any robust program.

### Models
Base_Model
Engine








#### A Holberton School project
