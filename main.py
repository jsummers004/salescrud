from unicodedata import numeric
from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import datetime
from fastapi_crudrouter import SQLAlchemyCRUDRouter
import models
import pydanticmodels
from fastapi import FastAPI
from database import SessionLocal

app = FastAPI()

"""
class RefState(BaseModel): #serializer
    state_id:Optional[str]
    name:str = Field(
        title="The name of the state", max_length=300
    )

    class Config:
        orm_mode = True

class RefStateCreate(RefState): #serializer
    created_by:int

    class Config:
        orm_mode = True

class RefStateUpdate(RefState): #serializer
    modified_by:int

    class Config:
        orm_mode = True

"""


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()



router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.Attachment,
    create_schema=pydanticmodels.AttachmentCreate,
    update_schema=pydanticmodels.AttachmentUpdate,
    db_model=models.AttachmentModel,
    db=get_db,
    prefix='Attachment'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.Branding,
    create_schema=pydanticmodels.BrandingCreate,
    update_schema=pydanticmodels.BrandingUpdate,
    db_model=models.BrandingModel,
    db=get_db,
    prefix='Branding'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.Customer,
    create_schema=pydanticmodels.CustomerCreate,
    update_schema=pydanticmodels.CustomerUpdate,
    db_model=models.CustomerModel,
    db=get_db,
    prefix='Customer'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.FeeTemplate,
    create_schema=pydanticmodels.FeeTemplateCreate,
    update_schema=pydanticmodels.FeeTemplateUpdate,
    db_model=models.FeeTemplateModel,
    db=get_db,
    prefix='FeeTemplate'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.FeeTemplateDetail,
    create_schema=pydanticmodels.FeeTemplateDetailCreate,
    update_schema=pydanticmodels.FeeTemplateDetailUpdate,
    db_model=models.FeeTemplateDetailModel,
    db=get_db,
    prefix='FeeTemplateDetail'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.Merchant,
    create_schema=pydanticmodels.MerchantCreate,
    update_schema=pydanticmodels.MerchantUpdate,
    db_model=models.MerchantModel,
    db=get_db,
    prefix='Merchant'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.MerchantAddress,
    create_schema=pydanticmodels.MerchantAddressCreate,
    update_schema=pydanticmodels.MerchantAddressUpdate,
    db_model=models.MerchantAddressModel,
    db=get_db,
    prefix='MerchantAddress'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.MerchantBank,
    create_schema=pydanticmodels.MerchantBankCreate,
    update_schema=pydanticmodels.MerchantBankUpdate,
    db_model=models.MerchantBankModel,
    db=get_db,
    prefix='MerchantBank'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.MerchantBoardingPlatform,
    create_schema=pydanticmodels.MerchantBoardingPlatformCreate,
    update_schema=pydanticmodels.MerchantBoardingPlatformUpdate,
    db_model=models.MerchantBoardingPlatformModel,
    db=get_db,
    prefix='MerchantBoardingPlatform'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.MerchantContact,
    create_schema=pydanticmodels.MerchantContactCreate,
    update_schema=pydanticmodels.MerchantContactUpdate,
    db_model=models.MerchantContactModel,
    db=get_db,
    prefix='MerchantContact'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.MerchantFees,
    create_schema=pydanticmodels.MerchantFeesCreate,
    update_schema=pydanticmodels.MerchantFeesUpdate,
    db_model=models.MerchantFeesModel,
    db=get_db,
    prefix='MerchantFees'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.MerchantProduct,
    create_schema=pydanticmodels.MerchantProductCreate,
    update_schema=pydanticmodels.MerchantProductUpdate,
    db_model=models.MerchantProductModel,
    db=get_db,
    prefix='MerchantProduct'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.Order,
    create_schema=pydanticmodels.OrderCreate,
    update_schema=pydanticmodels.OrderUpdate,
    db_model=models.OrderModel,
    db=get_db,
    prefix='Order'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.OrderLine,
    create_schema=pydanticmodels.OrderLineCreate,
    update_schema=pydanticmodels.OrderLineUpdate,
    db_model=models.OrderLineModel,
    db=get_db,
    prefix='OrderLine'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.Pricing,
    create_schema=pydanticmodels.PricingCreate,
    update_schema=pydanticmodels.PricingUpdate,
    db_model=models.PricingModel,
    db=get_db,
    prefix='Pricing'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.ProductConfig,
    create_schema=pydanticmodels.ProductConfigCreate,
    update_schema=pydanticmodels.ProductConfigUpdate,
    db_model=models.ProductConfigModel,
    db=get_db,
    prefix='ProductConfig'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefAddressType,
    create_schema=pydanticmodels.RefAddressTypeCreate,
    update_schema=pydanticmodels.RefAddressTypeUpdate,
    db_model=models.RefAddressTypeModel,
    db=get_db,
    prefix='RefAddressType'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefAttachmentType,
    create_schema=pydanticmodels.RefAttachmentTypeCreate,
    update_schema=pydanticmodels.RefAttachmentTypeUpdate,
    db_model=models.RefAttachmentTypeModel,
    db=get_db,
    prefix='RefAttachmentType'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefBackEndPlatform,
    create_schema=pydanticmodels.RefBackEndPlatformCreate,
    update_schema=pydanticmodels.RefBackEndPlatformUpdate,
    db_model=models.RefBackEndPlatformModel,
    db=get_db,
    prefix='RefBackEndPlatform'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefCardType,
    create_schema=pydanticmodels.RefCardTypeCreate,
    update_schema=pydanticmodels.RefCardTypeUpdate,
    db_model=models.RefCardTypeModel,
    db=get_db,
    prefix='RefCardType'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefConfigType,
    create_schema=pydanticmodels.RefConfigTypeCreate,
    update_schema=pydanticmodels.RefConfigTypeUpdate,
    db_model=models.RefConfigTypeModel,
    db=get_db,
    prefix='RefConfigType'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefFee,
    create_schema=pydanticmodels.RefFeeCreate,
    update_schema=pydanticmodels.RefFeeUpdate,
    db_model=models.RefFeeModel,
    db=get_db,
    prefix='RefFee'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefMbpBackEnd,
    create_schema=pydanticmodels.RefMbpBackEndCreate,
    update_schema=pydanticmodels.RefMbpBackEndUpdate,
    db_model=models.RefMbpBackEndModel,
    db=get_db,
    prefix='RefMbpBackEnd'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefMcc,
    create_schema=pydanticmodels.RefMccCreate,
    update_schema=pydanticmodels.RefMccUpdate,
    db_model=models.RefMccModel,
    db=get_db,
    prefix='RefMcc'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefMerchantStatus,
    create_schema=pydanticmodels.RefMerchantStatusCreate,
    update_schema=pydanticmodels.RefMerchantStatusUpdate,
    db_model=models.RefMerchantStatusModel,
    db=get_db,
    prefix='RefMerchantStatus'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefOrderStatus,
    create_schema=pydanticmodels.RefOrderStatusCreate,
    update_schema=pydanticmodels.RefOrderStatusUpdate,
    db_model=models.RefOrderStatusModel,
    db=get_db,
    prefix='RefOrderStatus'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefOwnershipType,
    create_schema=pydanticmodels.RefOwnershipTypeCreate,
    update_schema=pydanticmodels.RefOwnershipTypeUpdate,
    db_model=models.RefOwnershipTypeModel,
    db=get_db,
    prefix='RefOwnershipType'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefPermission,
    create_schema=pydanticmodels.RefPermissionCreate,
    update_schema=pydanticmodels.RefPermissionUpdate,
    db_model=models.RefPermissionModel,
    db=get_db,
    prefix='RefPermission'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefProcessor,
    create_schema=pydanticmodels.RefProcessorCreate,
    update_schema=pydanticmodels.RefProcessorUpdate,
    db_model=models.RefProcessorModel,
    db=get_db,
    prefix='RefProcessor'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefProduct,
    create_schema=pydanticmodels.RefProductCreate,
    update_schema=pydanticmodels.RefProductUpdate,
    db_model=models.RefProductModel,
    db=get_db,
    prefix='RefProduct'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefProductDelivery,
    create_schema=pydanticmodels.RefProductDeliveryCreate,
    update_schema=pydanticmodels.RefProductDeliveryUpdate,
    db_model=models.RefProductDeliveryModel,
    db=get_db,
    prefix='RefProductDelivery'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefProductType,
    create_schema=pydanticmodels.RefProductTypeCreate,
    update_schema=pydanticmodels.RefProductTypeUpdate,
    db_model=models.RefProductTypeModel,
    db=get_db,
    prefix='RefProductType'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefRefundPolicy,
    create_schema=pydanticmodels.RefRefundPolicyCreate,
    update_schema=pydanticmodels.RefRefundPolicyUpdate,
    db_model=models.RefRefundPolicyModel,
    db=get_db,
    prefix='RefRefundPolicy'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefSalesPersonType,
    create_schema=pydanticmodels.RefSalesPersonTypeCreate,
    update_schema=pydanticmodels.RefSalesPersonTypeUpdate,
    db_model=models.RefSalesPersonTypeModel,
    db=get_db,
    prefix='RefSalesPersonType'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefScheduleA,
    create_schema=pydanticmodels.RefScheduleACreate,
    update_schema=pydanticmodels.RefScheduleAUpdate,
    db_model=models.RefScheduleAModel,
    db=get_db,
    prefix='RefScheduleA'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefScheduleAMap,
    create_schema=pydanticmodels.RefScheduleAMapCreate,
    update_schema=pydanticmodels.RefScheduleAMapUpdate,
    db_model=models.RefScheduleAMapModel,
    db=get_db,
    prefix='RefScheduleAMap'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefServicesProvidedIn,
    create_schema=pydanticmodels.RefServicesProvidedInCreate,
    update_schema=pydanticmodels.RefServicesProvidedInUpdate,
    db_model=models.RefServicesProvidedInModel,
    db=get_db,
    prefix='RefServicesProvidedIn'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefState,
    create_schema=pydanticmodels.RefStateCreate,
    update_schema=pydanticmodels.RefStateUpdate,
    db_model=models.RefStateModel,
    db=get_db,
    prefix='RefState'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefTicketReason,
    create_schema=pydanticmodels.RefTicketReasonCreate,
    update_schema=pydanticmodels.RefTicketReasonUpdate,
    db_model=models.RefTicketReasonModel,
    db=get_db,
    prefix='RefTicketReason'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefTicketStatus,
    create_schema=pydanticmodels.RefTicketStatusCreate,
    update_schema=pydanticmodels.RefTicketStatusUpdate,
    db_model=models.RefTicketStatusModel,
    db=get_db,
    prefix='RefTicketStatus'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefUserType,
    create_schema=pydanticmodels.RefUserTypeCreate,
    update_schema=pydanticmodels.RefUserTypeUpdate,
    db_model=models.RefUserTypeModel,
    db=get_db,
    prefix='RefUserType'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RefWhenCardCharged,
    create_schema=pydanticmodels.RefWhenCardChargedCreate,
    update_schema=pydanticmodels.RefWhenCardChargedUpdate,
    db_model=models.RefWhenCardChargedModel,
    db=get_db,
    prefix='RefWhenCardCharged'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RepCodeBoardingPlatform,
    create_schema=pydanticmodels.RepCodeBoardingPlatformCreate,
    update_schema=pydanticmodels.RepCodeBoardingPlatformUpdate,
    db_model=models.RepCodeBoardingPlatformModel,
    db=get_db,
    prefix='RepCodeBoardingPlatform'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RepScheduleA,
    create_schema=pydanticmodels.RepScheduleACreate,
    update_schema=pydanticmodels.RepScheduleAUpdate,
    db_model=models.RepScheduleAModel,
    db=get_db,
    prefix='RepScheduleA'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.RepScheduleAItem,
    create_schema=pydanticmodels.RepScheduleAItemCreate,
    update_schema=pydanticmodels.RepScheduleAItemUpdate,
    db_model=models.RepScheduleAItemModel,
    db=get_db,
    prefix='RepScheduleAItem'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.SalesOffice,
    create_schema=pydanticmodels.SalesOfficeCreate,
    update_schema=pydanticmodels.SalesOfficeUpdate,
    db_model=models.SalesOfficeModel,
    db=get_db,
    prefix='SalesOffice'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.SalesPerson,
    create_schema=pydanticmodels.SalesPersonCreate,
    update_schema=pydanticmodels.SalesPersonUpdate,
    db_model=models.SalesPersonModel,
    db=get_db,
    prefix='SalesPerson'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.SalesPersonRep,
    create_schema=pydanticmodels.SalesPersonRepCreate,
    update_schema=pydanticmodels.SalesPersonRepUpdate,
    db_model=models.SalesPersonRepModel,
    db=get_db,
    prefix='SalesPersonRep'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.SeasonalBusiness,
    create_schema=pydanticmodels.SeasonalBusinessCreate,
    update_schema=pydanticmodels.SeasonalBusinessUpdate,
    db_model=models.SeasonalBusinessModel,
    db=get_db,
    prefix='SeasonalBusiness'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.Ticket,
    create_schema=pydanticmodels.TicketCreate,
    update_schema=pydanticmodels.TicketUpdate,
    db_model=models.TicketModel,
    db=get_db,
    prefix='Ticket'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.TicketComment,
    create_schema=pydanticmodels.TicketCommentCreate,
    update_schema=pydanticmodels.TicketCommentUpdate,
    db_model=models.TicketCommentModel,
    db=get_db,
    prefix='TicketComment'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.UserRole,
    create_schema=pydanticmodels.UserRoleCreate,
    update_schema=pydanticmodels.UserRoleUpdate,
    db_model=models.UserRoleModel,
    db=get_db,
    prefix='UserRole'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.UserRolePermission,
    create_schema=pydanticmodels.UserRolePermissionCreate,
    update_schema=pydanticmodels.UserRolePermissionUpdate,
    db_model=models.UserRolePermissionModel,
    db=get_db,
    prefix='UserRolePermission'
)

app.include_router(router)


router = SQLAlchemyCRUDRouter(
    schema=pydanticmodels.Users,
    create_schema=pydanticmodels.UsersCreate,
    update_schema=pydanticmodels.UsersUpdate,
    db_model=models.UsersModel,
    db=get_db,
    prefix='Users'
)

app.include_router(router)
