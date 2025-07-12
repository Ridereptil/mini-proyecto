from db.db import init_db
from views.main import create_main_window
from db.db import  init_db
init_db()

app = create_main_window()
app.mainloop()