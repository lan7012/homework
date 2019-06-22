import pymongo
from  pymongo.collection import Collection

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
db = client['douyin']

def handle_init_task():
    task_id_collection = Collection(db, 'task_id')
    with open('douyin_hot_id.txt', 'r')as f_share:
        for f_share_task in f_share.readlines():
            init_task = {}
            init_task['share_id'] = f_share_task.replace('\n', '')
            task_id_collection.insert(init_task)

def handle_get_tesk():
    task_id_collection = Collection(db, 'task_id')
    return task_id_collection.find_one({})

#handle_init_task()
print(handle_get_tesk())