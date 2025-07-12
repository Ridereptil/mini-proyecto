from db.db import init_db
from views.main import create_main_window
from db.db import  init_db
# Inicializar la base de datos
init_db()

# Crear y mostrar la ventana principal
app = create_main_window()
app.mainloop()