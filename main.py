from fastapi import FastAPI
from Apis.Api_EstadoPaciente import router as EstadopacienteRouter
from Apis.Api_Habitacion import router as HabitacionRouter
from Apis.Api_HistorialRegistroVisitante import router as historialvisitanteRouter
from Apis.Api_Hospitalizacion import router as hospitalizacionRouter
from Apis.Api_Paciente import router as pacienteRouter
from Apis.Api_Perfil_Usuario import router as perfilUsuarioRouter
from Apis.Api_RegistroVisitas import router as RegistroVisitaRouter
from Apis.Api_Roles import router as rolesRouter
from Apis.Api_Visitante import router as visitanteRouter
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Incluir el router de EstadoPaciente con el prefijo /estadopaciente
app.include_router(EstadopacienteRouter, prefix="/estadopaciente")
# Incluir el router de Habitacion con el prefijo /habitacion
app.include_router(HabitacionRouter, prefix="/habitacion")
app.include_router(historialvisitanteRouter, prefix="/HistorialVisitante")
app.include_router(hospitalizacionRouter, prefix="/Hospitalizacion")
app.include_router(pacienteRouter, prefix="/pacientes")
app.include_router(perfilUsuarioRouter, prefix="/PerfilUsuario")
app.include_router(RegistroVisitaRouter, prefix="/RegistroVisitas")
app.include_router(rolesRouter, prefix="/roles")
app.include_router(visitanteRouter, prefix="/visitantes")



