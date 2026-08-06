# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from app.core.config import settings
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from app.crud.transaction_crud import create_transaction, get_transaction, get_transactions, update_transaction, delete_transaction
from app.dependencies import get_db

app = FastAPI(title=settings.PROJECT_NAME, version=settings.API_VERSION)


@app.post("/transactions/", response_model=Transaction)
def create_transaction_endpoint(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction(db=db, transaction=transaction)


@app.get("/transactions/{transaction_id}", response_model=Transaction)
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    db_transaction = get_transaction(db, transaction_id)
    if db_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return db_transaction


@app.get("/transactions/", response_model=List[Transaction])
def read_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    transactions = get_transactions(db, skip=skip, limit=limit)
    return transactions


@app.put("/transactions/{transaction_id}", response_model=Transaction)
def update_transaction_endpoint(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    updated_transaction = update_transaction(db=db, transaction_id=transaction_id, transaction=transaction)
    if updated_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated_transaction


@app.delete("/transactions/{transaction_id}")
def delete_transaction_endpoint(transaction_id: int, db: Session = Depends(get_db)):
    deleted = delete_transaction(db=db, transaction_id=transaction_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"detail": "Transaction deleted"}

// === ARCHIVO: app/__init__.py ===

# Inicializador del paquete principal de la aplicación

// === ARCHIVO: app/core/__init__.py ===

# Inicializador del paquete core

// === ARCHIVO: app/dependencies/__init__.py ===

from sqlalchemy.orm import Session
from app.core.config import settings
from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

// === ARCHIVO: app/models/__init__.py ===

# Inicializador del paquete de modelos de datos

// === ARCHIVO: app/models/transaction.py ===

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, index=True)
    status = Column(String, index=True)
    timestamp = Column(DateTime, index=True)

// === ARCHIVO: app/schemas/__init__.py ===

# Inicializador del paquete de esquemas de datos

// === ARCHIVO: app/schemas/transaction.py ===

from pydantic import BaseModel
from typing import Optional


class TransactionBase(BaseModel):
    amount: int
    status: str


class TransactionCreate(TransactionBase):
    pass


class TransactionUpdate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int
    timestamp: str

    class Config:
        orm_mode = True

// === ARCHIVO: app/services/__init__.py ===

# Inicializador del paquete de servicios

// === ARCHIVO: app/services/transaction_service.py ===

from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from app.crud.transaction_crud import create_transaction, get_transaction, get_transactions, update_transaction, delete_transaction


def create_transaction_service(db: Session, transaction: TransactionCreate):
    return create_transaction(db, transaction)


def get_transaction_service(db: Session, transaction_id: int):
    return get_transaction(db, transaction_id)


def get_transactions_service(db: Session, skip: int = 0, limit: int = 10):
    return get_transactions(db, skip, limit)


def update_transaction_service(db: Session, transaction_id: int, transaction: TransactionUpdate):
    return update_transaction(db, transaction_id, transaction)


def delete_transaction_service(db: Session, transaction_id: int):
    return delete_transaction(db, transaction_id)

// === ARCHIVO: app/crud/__init__.py ===

# Inicializador del paquete de CRUD

// === ARCHIVO: app/crud/transaction_crud.py ===

from sqlalchemy.orm import Session
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate


def create_transaction(db: Session, transaction: TransactionCreate):
    db_transaction = Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.id == transaction_id).first()


def get_transactions(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Transaction).offset(skip).limit(limit).all()


def update_transaction(db: Session, transaction_id: int, transaction: TransactionUpdate):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction is None:
        return None
    for key, value in transaction.dict().items():
        setattr(db_transaction, key, value)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction


def delete_transaction(db: Session, transaction_id: int):
    db_transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if db_transaction is None:
        return False
    db.delete(db_transaction)
    db.commit()
    return True

// === ARCHIVO: app/api/__init__.py ===

# Inicializador del paquete de API

// === ARCHIVO: app/api/transaction_api.py ===

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.config import settings
from app.models.transaction import Transaction
from app.schemas.transaction import TransactionCreate, TransactionUpdate
from app.services.transaction_service import create_transaction_service, get_transaction_service, get_transactions_service, update_transaction_service, delete_transaction_service
from app.dependencies import get_db


router = APIRouter()


@router.post("/transactions/")
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return create_transaction_service(db, transaction)


@router.get("/transactions/{transaction_id}")
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = get_transaction_service(db, transaction_id)
    if transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction


@router.get("/transactions/")
def read_transactions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    transactions = get_transactions_service(db, skip, limit)
    return transactions


@router.put("/transactions/{transaction_id}")
def update_transaction(transaction_id: int, transaction: TransactionUpdate, db: Session = Depends(get_db)):
    updated_transaction = update_transaction_service(db, transaction_id, transaction)
    if updated_transaction is None:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated_transaction


@router.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    deleted = delete_transaction_service(db, transaction_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"detail": "Transaction deleted"}

// === ARCHIVO: tests/__init__.py ===

# Inicializador del paquete de pruebas

// === ARCHIVO: tests/test_transaction_api.py ===

from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_create_transaction():
    response = client.post(
        "/transactions/",
        json={"amount": 100, "status": "pending"},
    )
    assert response.status_code == 200
    assert response.json().get('amount') == 100


def test_read_transaction():
    response = client.get("/transactions/1")
    assert response.status_code == 200
    assert response.json().get('amount') == 100


def test_read_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_update_transaction():
    response = client.put(
        "/transactions/1",
        json={"amount": 200, "status": "completed"},
    )
    assert response.status_code == 200
    assert response.json().get('amount') == 200


def test_delete_transaction():
    response = client.delete("/transactions/1")
    assert response.status_code == 200
    assert response.json().get('detail') == 'Transaction deleted'

// === ARCHIVO: config/__init__.py ===

# Inicializador del paquete de configuración

// === ARCHIVO: config/settings.py ===

from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = 'Payment API'
    API_VERSION: str = '0.1.0'
    DATABASE_URL: str

    class Config:
        env_file = '.env'

settings = Settings()

```
