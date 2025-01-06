1. Videos
    - Host?  -> Youtube
            -> Vimeo, Vistia
    - Analytics?  -> Lots of data 
                -> A user can watch 100 videos for 10 seconds = 10000
                -> Lots of writes 
                -> Frames by Frames : 30 FPS : 120 seconds : 3600 rows of data write ther, too many writes even for a single video 

                -> For such scenarios apache cassandra(astra db) will be the best: can handle large amount of data, handle too many wirtes and is scalable



2. Members
    - Sign up 
    - Login 
    - Remember things 
    - Email Validation 



Astra DB: Managed NoSQL cassandra
Contains:
    - Database name
        - keyspace name
            - Tables 
