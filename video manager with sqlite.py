import sqlite3
conn=sqlite3.connect('videos.db')
cursor=conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS VIDEO(
               VIDEO_ID INTEGER PRIMARY KEY,
               NAME TEXT NOT NULL,
               TIME TEXT NOT NULL
               )       
''')

def list_videos():
    cursor.execute('SELECT * FROM VIDEO')
    for row in cursor.fetchall():
        print(row)
    print(cursor.fetchall())

def add_video(name,time):
    cursor.execute('INSERT INTO VIDEO (name,time) VALUES (?,?)',(name,time))
    conn.commit()

def update_video(new_name,new_time,video_id):
    cursor.execute('UPDATE VIDEO SET name=?, time=? WHERE video_id=?',(new_name,new_time,video_id))
    conn.commit()
 
def delete_video(video_id):
    cursor.execute('DELETE FROM VIDEO WHERE id=?',(video_id,))
    conn.commit()

def main():
    while True:
        print('\n youtube manager | Select your choice')
        print('1. to list all the videos')
        print('2. to add a video')
        print('3. to update a video')
        print('4. to delete a video')
        print('5. exit')

        choice=input('Enter your choice: ')
        if choice=='1':
            list_videos()
        elif choice=='2':
            name= input('Enter video name: ')
            time= input('Enter video time: ')
            add_video(name,time)
        elif choice=='3':
            video_id= input('Enter the video id: ')
            name= input('Enter video name: ')
            time= input('Enter video time: ')
            update_video(video_id,name,time)
        elif choice=='4':
            video_id= input('Enter the video id: ')
            delete_video(video_id)
        else:
            break
    conn.close()
if __name__=='__main__':
    main()

