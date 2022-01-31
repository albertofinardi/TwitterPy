# import openpyxl and tkinter modules
from tkinter import *
import config_manager
import console
    
 
# Function to set focus (cursor)
def focus1(event):
    # set focus on the max_tweets box
    max_tweets.focus_set()
 
 
# Function to set focus
def focus2(event):
    # set focus on the min_likes box
    min_likes.focus_set()
 
 
# Function to set focus
def focus3(event):
    # set focus on the max_added_or_fetched box
    max_added_or_fetched.focus_set()
 
 
# Function to set focus
def focus4(event):
    # set focus on the query box
    query.focus_set()
 
 
# Function to set focus
def focus5(event):
    # set focus on the days_span box
    days_span.focus_set()
 
 
# Function to set focus
def focus6(event):
    # set focus on the export_csv box
    export_csv.focus_set()
# Function to set focus

def focus7(event):
    # set focus on the export_csv box
    export_json.focus_set()

# Function to set focus
def focus8(event):
    # set focus on the export_csv box
    backup_folder.focus_set()
# Function to set focus
def focus9(event):
    # set focus on the export_csv box
    export_csv_backup.focus_set()
# Function to set focus
def focus10(event):
    # set focus on the export_csv box
    export_json_backup.focus_set()
 
 
# Function to take data from GUI
# window and write to an excel file
def start():
     
    # if user not fill any entry
    # then print "empty input"
    if (bearer_token.get() == "" and
        max_tweets.get() == "" and
        min_likes.get() == "" and
        max_added_or_fetched.get() == "" and
        query.get() == "" and
        days_span.get() == "" and
        export_csv.get() == "" and
        export_json.get() == "" and backup_folder.get() == "" and export_csv_backup.get() == "" and export_json_backup.get() == ""):
             
        print("empty input")
 
    else:
        # Start program
        print('Start')
        config_manager.save(bearer_token.get(), max_tweets.get(), min_likes.get(), max_added_or_fetched.get(), query.get(), days_span.get(), export_csv.get(), export_json.get(), backup_folder.get(), export_csv_backup.get(), export_json_backup.get())
        console.start(bearer_token.get(), max_tweets.get(), min_likes.get(), max_added_or_fetched.get(), query.get(), days_span.get(), export_csv.get(), export_json.get(), backup_folder.get(), export_csv_backup.get(), export_json_backup.get())

# Driver code
if __name__ == "__main__":
     
    # create a GUI window
    root = Tk()
 
    # set the title of GUI window
    root.title("TwitterPy")
 
    # set the configuration of GUI window
    root.geometry("600x400")
 
 
    # create a Form label
    heading = Label(root, text="Form")
 
    # create a bearer_token_label label
    bearer_token_label = Label(root, text="Bearer token")
 
    # create a max_tweets_label label
    max_tweets_label = Label(root, text="Max tweets")
 
    # create a min_likes_labelester label
    min_likes_label = Label(root, text="Min likes")
 
    # create a Form No. label
    max_added_or_fetched_label = Label(root, text="Added/Fetched mode")
 
    # create a Contact No. label
    query_label = Label(root, text="Filters")
 
    # create a Email id label
    days_span_label = Label(root, text="Days span")
 
    # create a address label
    export_csv_label = Label(root, text="Export csv")
    
    # create a address label
    export_json_label = Label(root, text="Export json")
    
    # create a address label
    backup_folder_label = Label(root, text="Backup folder")
    
    # create a address label
    export_csv_backup_label = Label(root, text="Backup csv")
    
    # create a address label
    export_json_backup_label = Label(root, text="Backup json")
 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    heading.grid(row=0, column=1)
    bearer_token_label.grid(row=1, column=0)
    max_tweets_label.grid(row=2, column=0)
    min_likes_label.grid(row=3, column=0)
    max_added_or_fetched_label.grid(row=4, column=0)
    query_label.grid(row=5, column=0)
    days_span_label.grid(row=6, column=0)
    export_csv_label.grid(row=7, column=0)
    export_json_label.grid(row=8, column=0)
    backup_folder_label.grid(row=9, column=0)
    export_csv_backup_label.grid(row=10, column=0)
    export_json_backup_label.grid(row=11, column=0)


    # Variables
    #export_json_backup_var = StringVar(root, value=config.export_json_backup)
    #export_csv_backup_var = StringVar(root, value=config.export_csv_backup)
    #backup_folder_var = StringVar(root, value=config.backup_folder)
    #export_json_var = StringVar(root, value=config.export_json)
    #export_csv_var = StringVar(root, value=config.export_csv)
    #days_span_var = IntVar(root, value=config.days_span)
    #query_var = StringVar(root, value=config.query)
    #max_added_or_fetched_var = StringVar(root, value=config.max_added_or_fetched)
    #min_likes_var = IntVar(root, value=config.min_likes)
    #max_tweets_var = StringVar(root, value=config.max_tweets)
    #bearer_token_var = StringVar(root, value=config.bearer_token)

    bearer_token_var,max_tweets_var,min_likes_var,max_added_or_fetched_var,query_var,days_span_var,export_csv_var,export_json_var,backup_folder_var,export_csv_backup_var,export_json_backup_var = config_manager.config()
    
    export_json_backup_var = StringVar(root, value=export_json_backup_var)
    export_csv_backup_var = StringVar(root, value=export_csv_backup_var)
    backup_folder_var = StringVar(root, value=backup_folder_var)
    export_json_var = StringVar(root, value=export_json_var)
    export_csv_var = StringVar(root, value=export_csv_var)
    days_span_var = IntVar(root, value=days_span_var)
    query_var = StringVar(root, value=query_var)
    max_added_or_fetched_var = StringVar(root, value=max_added_or_fetched_var)
    min_likes_var = IntVar(root, value=min_likes_var)
    max_tweets_var = StringVar(root, value=max_tweets_var)
    bearer_token_var = StringVar(root, value=bearer_token_var)

    # create a text entry box
    # for typing the information
    bearer_token = Entry(root, textvariable=bearer_token_var)
    max_tweets = Entry(root, textvariable=max_tweets_var)
    min_likes = Entry(root, textvariable=min_likes_var)
    max_added_or_fetched = Entry(root, textvariable=max_added_or_fetched_var)
    query = Entry(root, textvariable=query_var)
    days_span = Entry(root, textvariable=days_span_var)
    export_csv = Entry(root, textvariable=export_csv_var)
    export_json = Entry(root, textvariable=export_json_var)
    backup_folder = Entry(root, textvariable=backup_folder_var)
    export_csv_backup = Entry(root, textvariable=export_csv_backup_var)
    export_json_backup = Entry(root, textvariable=export_json_backup_var)
 
    # bind method of widget is used for
    # the binding the function with the events
 
    # whenever the enter key is pressed
    # then call the focus1 function
    bearer_token.bind("<Return>", focus1)
 
    # whenever the enter key is pressed
    # then call the focus2 function
    max_tweets.bind("<Return>", focus2)
 
    # whenever the enter key is pressed
    # then call the focus3 function
    min_likes.bind("<Return>", focus3)
 
    # whenever the enter key is pressed
    # then call the focus4 function
    max_added_or_fetched.bind("<Return>", focus4)
 
    # whenever the enter key is pressed
    # then call the focus5 function
    query.bind("<Return>", focus5)
 
    # whenever the enter key is pressed
    # then call the focus6 function
    days_span.bind("<Return>", focus6)
    # whenever the enter key is pressed
    # then call the focus6 function
    export_csv.bind("<Return>", focus7)
 
    # whenever the enter key is pressed
    # then call the focus6 function
    export_json.bind("<Return>", focus8)
    # whenever the enter key is pressed
    # then call the focus6 function
    backup_folder.bind("<Return>", focus9)
    # whenever the enter key is pressed
    # then call the focus6 function
    export_csv_backup.bind("<Return>", focus10)

 
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    bearer_token.grid(row=1, column=1, ipadx="100")
    max_tweets.grid(row=2, column=1, ipadx="100")
    min_likes.grid(row=3, column=1, ipadx="100")
    max_added_or_fetched.grid(row=4, column=1, ipadx="100")
    query.grid(row=5, column=1, ipadx="100")
    days_span.grid(row=6, column=1, ipadx="100")
    export_csv.grid(row=7, column=1, ipadx="100")
    export_json.grid(row=8, column=1, ipadx="100")
    backup_folder.grid(row=9, column=1, ipadx="100")
    export_csv_backup.grid(row=10, column=1, ipadx="100")
    export_json_backup.grid(row=11, column=1, ipadx="100")
 
    # create a Submit Button and place into the root window
    submit = Button(root, text="Start", command=start)
    submit.grid(row=12, column=1)
 
    # start the GUI
    root.mainloop()