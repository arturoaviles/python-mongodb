# Python + Mongo

On this tutorial we will create an API using Python 3 and MongoDB

## Requirements

* [Python 3][python3_download]
* [MongoDB][mongodb_download]

## Getting Started

1. Create a Python Virtual Environment.

```bash
pip3 install virtualenv
virtualenv -p python3 my-vir-env-py-mon
```

2. Activate and go inside your Virtual Environment

```bash
source my-vir-env-py-mon/bin/activate
cd my-vir-env-py-mon
```

3. Clone this project

```bash
git clone 
```

4. Install dependencies

```bash
pip install -r requirements.txt
``` 

5. Make a copy of the env.sample to .env

```
cp env.sample .env
```

6. Configure the .env with your MongoDB Credentials


```
DATABASE=Your_DB_Name
PASSWORD=Your_DB_Pass
```


7. Run the API

```
python app.py
```

## More Tutorials

* [MongoDB (Youtube Channel)](https://www.youtube.com/user/MongoDB)
* [Data Wrangling with MongoDB (Udacity)](https://www.udacity.com/course/data-wrangling-with-mongodb--ud032)
* [How to Install and Secure MongoDB on Ubuntu 16.04 (Digital Ocean)](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-mongodb-on-ubuntu-16-04)
* [How To Back Up, Restore, and Migrate a MongoDB Database on Ubuntu 14.04 (Digital Ocean)](https://www.digitalocean.com/community/tutorials/how-to-back-up-restore-and-migrate-a-mongodb-database-on-ubuntu-14-04)

## License

This sample code is licensed under MIT
Full license text is available in [LICENSE](LICENSE).

[python3_download]:(https://www.python.org/downloads/)
[mongodb_download]:(https://www.mongodb.com/)





