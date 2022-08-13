from .dynamic_fields_serializer import DFModelSerializer
from .user import UserBaseSerializer, UserReadSerializer, UserSerializer
from .usuario import UsuarioBaseSerializer, UsuarioReadSerializer, UsuarioSaveSerializer
from .sector import SectorBaseSerializer, SectorReadSerializer, SectorSaveSerializer
from .configuracion import  ConfiguracionReadSerializer, ConfiguracionSaveSerializer
from .proyecto import ProyectoBaseSerializer, ProyectoReadSerializer, ProyectoSaveSerializer
from .servicio import ServicioBaseSerializer, ServicioReadSerializer, ServicioSaveSerializer
from .detalle import DetalleBaseSerializer, DetalleReadSerializer, DetalleSaveSerializer
from .pago import PagoBaseSerializer, PagoReadSerializer, PagoSaveSerializer