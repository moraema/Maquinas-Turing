from fasthtml.common import *
from Turing_Machine import Turing_Machine
from states import initial_state, final_states, transitions

app, rt = fast_app()

@rt('/l')
def get(): return Div(P('Hello World!'), hx_get="/change")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@rt('/', methods=["GET", "POST"])
async def index(request: Request):
    result = None


    if request.method == "POST":
       
        form_data = await request.form()
        input_cinta = form_data.get("cinta", "")

        
        machine = Turing_Machine(input_cinta, initial_state, final_states, transitions)
        machine.run()
        
       
        result = machine.is_valid()

    
    return "Reultado: " + result if result else "Cadena no aceptada, verique que la cadena corresponda con lo indicado"


serve()