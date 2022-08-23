from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class RefOrderStatus(BaseModel):
    
    order_status_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefOrderStatusCreate(BaseModel):
    
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefOrderStatusUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefRefundPolicy(BaseModel):
    
    refund_policy_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefRefundPolicyCreate(BaseModel):
    
    refund_policy_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefRefundPolicyUpdate(BaseModel):
    
    refund_policy_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefProductDelivery(BaseModel):
    
    product_delivery_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefProductDeliveryCreate(BaseModel):
    
    product_delivery_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefProductDeliveryUpdate(BaseModel):
    
    product_delivery_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefOwnershipType(BaseModel):
    
    ownership_type_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefOwnershipTypeCreate(BaseModel):
    
    ownership_type_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefOwnershipTypeUpdate(BaseModel):
    
    ownership_type_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefMerchantStatus(BaseModel):
    
    merchant_status_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefMerchantStatusCreate(BaseModel):
    
    merchant_status_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefMerchantStatusUpdate(BaseModel):
    
    merchant_status_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefPermission(BaseModel):
    
    permission_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefPermissionCreate(BaseModel):
    
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefPermissionUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefTicketStatus(BaseModel):
    
    ticket_status_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefTicketStatusCreate(BaseModel):
    
    ticket_status_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefTicketStatusUpdate(BaseModel):
    
    ticket_status_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefFee(BaseModel):
    
    fee_id:int
    fee_category:str=Field(max_length=15)
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefFeeCreate(BaseModel):
    
    fee_category:str=Field(max_length=15)
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefFeeUpdate(BaseModel):
    
    fee_category:str=Field(max_length=15)
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefAddressType(BaseModel):
    
    address_type_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefAddressTypeCreate(BaseModel):
    
    address_type_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefAddressTypeUpdate(BaseModel):
    
    address_type_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefTicketReason(BaseModel):
    
    ticket_reason_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefTicketReasonCreate(BaseModel):
    
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefTicketReasonUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class MerchantBoardingPlatform(BaseModel):
    
    mbp_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class MerchantBoardingPlatformCreate(BaseModel):
    
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class MerchantBoardingPlatformUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefBackEndPlatform(BaseModel):
    
    back_end_platform_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefBackEndPlatformCreate(BaseModel):
    
    back_end_platform_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefBackEndPlatformUpdate(BaseModel):
    
    back_end_platform_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefMbpBackEnd(BaseModel):
    
    mbp_back_end_id:int
    mbp_id:int
    mbp_ref:Optional[MerchantBoardingPlatform]
    back_end_platform_id:int
    back_end_platform_ref:Optional[RefBackEndPlatform]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefMbpBackEndCreate(BaseModel):
    
    mbp_id:int
    back_end_platform_id:int
    created_by:int
    class Config:
        orm_mode = True
    
class RefMbpBackEndUpdate(BaseModel):
    
    mbp_id:int
    back_end_platform_id:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefConfigType(BaseModel):
    
    config_type_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefConfigTypeCreate(BaseModel):
    
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefConfigTypeUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefProductType(BaseModel):
    
    product_type_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefProductTypeCreate(BaseModel):
    
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefProductTypeUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefProduct(BaseModel):
    
    product_id:int
    product_type_id:int
    product_type_ref:Optional[RefProductType]
    name:str=Field(max_length=30)
    image:Optional[str]=Field(max_length=250)
    description:Optional[str]
    features:Optional[str]
    default_price:Optional[int]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefProductCreate(BaseModel):
    
    product_type_id:int
    name:str=Field(max_length=30)
    image:Optional[str]=Field(max_length=250)
    description:Optional[str]
    features:Optional[str]
    default_price:Optional[int]
    created_by:int
    class Config:
        orm_mode = True
    
class RefProductUpdate(BaseModel):
    
    product_type_id:int
    name:str=Field(max_length=30)
    image:Optional[str]=Field(max_length=250)
    description:Optional[str]
    features:Optional[str]
    default_price:Optional[int]
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefScheduleA(BaseModel):
    
    schedule_a_id:int
    name:str=Field(max_length=30)
    cost_type:str=Field(max_length=15)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefScheduleACreate(BaseModel):
    
    name:str=Field(max_length=30)
    cost_type:str=Field(max_length=15)
    created_by:int
    class Config:
        orm_mode = True
    
class RefScheduleAUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    cost_type:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefProcessor(BaseModel):
    
    processor_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefProcessorCreate(BaseModel):
    
    processor_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefProcessorUpdate(BaseModel):
    
    processor_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefScheduleAMap(BaseModel):
    
    schedule_a_map_id:int
    schedule_a_id:int
    schedule_a_ref:Optional[RefScheduleA]
    processor_id:int
    processor_ref:Optional[RefProcessor]
    fee_code:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefScheduleAMapCreate(BaseModel):
    
    schedule_a_id:int
    processor_id:int
    fee_code:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefScheduleAMapUpdate(BaseModel):
    
    schedule_a_id:int
    processor_id:int
    fee_code:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefCardType(BaseModel):
    
    card_type_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefCardTypeCreate(BaseModel):
    
    card_type_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefCardTypeUpdate(BaseModel):
    
    card_type_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefAttachmentType(BaseModel):
    
    attachment_type_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefAttachmentTypeCreate(BaseModel):
    
    attachment_type_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefAttachmentTypeUpdate(BaseModel):
    
    attachment_type_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefState(BaseModel):
    
    state_id:int
    state_code:str=Field(max_length=2)
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefStateCreate(BaseModel):
    
    state_code:str=Field(max_length=2)
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefStateUpdate(BaseModel):
    
    state_code:str=Field(max_length=2)
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefUserType(BaseModel):
    
    user_type_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefUserTypeCreate(BaseModel):
    
    user_type_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefUserTypeUpdate(BaseModel):
    
    user_type_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefSalesPersonType(BaseModel):
    
    sales_person_type_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefSalesPersonTypeCreate(BaseModel):
    
    sales_person_type_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefSalesPersonTypeUpdate(BaseModel):
    
    sales_person_type_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefMcc(BaseModel):
    
    mcc_id:int
    name:str=Field(max_length=255)
    mcc_code:str=Field(max_length=15)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefMccCreate(BaseModel):
    
    name:str=Field(max_length=100)
    mcc_code:str=Field(max_length=15)
    created_by:int
    class Config:
        orm_mode = True
    
class RefMccUpdate(BaseModel):
    
    name:str=Field(max_length=100)
    mcc_code:str=Field(max_length=15)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefWhenCardCharged(BaseModel):
    
    when_card_charged_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefWhenCardChargedCreate(BaseModel):
    
    when_card_charged_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefWhenCardChargedUpdate(BaseModel):
    
    when_card_charged_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RefServicesProvidedIn(BaseModel):
    
    services_provided_in_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RefServicesProvidedInCreate(BaseModel):
    
    services_provided_in_id:int
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RefServicesProvidedInUpdate(BaseModel):
    
    services_provided_in_id:int
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RepCodeBoardingPlatform(BaseModel):
    
    rep_code_boarding_platform_id:int
    rep_code:str=Field(max_length=15)
    name:str=Field(max_length=30)
    mbp_id:int
    mbp_ref:Optional[MerchantBoardingPlatform]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RepCodeBoardingPlatformCreate(BaseModel):
    
    rep_code:str=Field(max_length=15)
    name:str=Field(max_length=30)
    mbp_id:int
    created_by:int
    class Config:
        orm_mode = True
    
class RepCodeBoardingPlatformUpdate(BaseModel):
    
    rep_code:str=Field(max_length=15)
    name:str=Field(max_length=30)
    mbp_id:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class Branding(BaseModel):
    
    branding_id:int
    name:str=Field(max_length=30)
    logo:Optional[str]=Field(max_length=200)
    contact_phone:str=Field(max_length=15)
    contact_email:str=Field(max_length=50)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class BrandingCreate(BaseModel):
    
    name:str=Field(max_length=30)
    logo:Optional[str]=Field(max_length=200)
    contact_phone:str=Field(max_length=15)
    contact_email:str=Field(max_length=50)
    created_by:int
    class Config:
        orm_mode = True
    
class BrandingUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    logo:Optional[str]=Field(max_length=200)
    contact_phone:str=Field(max_length=15)
    contact_email:str=Field(max_length=50)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class Customer(BaseModel):
    
    customer_id:int
    name:str=Field(max_length=30)
    branding_id:Optional[int]
    branding_ref:Optional[Branding]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class CustomerCreate(BaseModel):
    
    name:str=Field(max_length=30)
    branding_id:Optional[int]
    created_by:int
    class Config:
        orm_mode = True
    
class CustomerUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    branding_id:Optional[int]
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class Merchant(BaseModel):
    
    merchant_id:int
    dba_name:str=Field(max_length=100)
    legal_name:Optional[str]=Field(max_length=100)
    tax_filing_name:Optional[str]=Field(max_length=100)
    tax_id_token:Optional[str]=Field(max_length=100)
    business_start_date:Optional[str]
    website:Optional[str]=Field(max_length=150)
    phone_number:Optional[str]=Field(max_length=15)
    fax:Optional[str]=Field(max_length=15)
    business_license_number:Optional[str]=Field(max_length=30)
    business_license_state_id:Optional[str]=Field(max_length=2)
    business_license_state_ref:Optional[RefState]
    rep_code:str=Field(max_length=15)
    rep_code_ref:Optional[RepCodeBoardingPlatform]
    mcc_id:Optional[int]
    mcc_ref:Optional[RefMcc]
    business_desc:Optional[str]
    when_card_charged_id:Optional[str]=Field(max_length=15)
    when_card_charged_ref:Optional[RefWhenCardCharged]
    services_provided_in_id:Optional[str]=Field(max_length=15)
    services_provided_in_ref:Optional[RefServicesProvidedIn]
    annual_volume:Optional[int]
    average_ticket:Optional[int]
    high_ticket:Optional[int]
    refund_policy_id:Optional[str]=Field(max_length=15)
    refund_policy_ref:Optional[RefRefundPolicy]
    is_seasonal:bool
    product_delivery_id:Optional[str]=Field(max_length=15)
    product_delivery_ref:Optional[RefProductDelivery]
    in_person_pct:Optional[int]
    online_pct:Optional[int]
    telephone_pct:Optional[int]
    ownership_type:Optional[str]=Field(max_length=15)
    ownership_type_ref:Optional[RefOwnershipType]
    back_end_platform_id:Optional[str]=Field(max_length=15)
    back_end_platform_ref:Optional[RefBackEndPlatform]
    customer_id:int
    customer_ref:Optional[Customer]
    merchant_status_id:int
    merchant_status_ref:Optional[RefMerchantStatus]
    priority:bool
    branding_id:int
    branding_ref:Optional[Branding]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class MerchantCreate(BaseModel):
    
    dba_name:str=Field(max_length=100)
    legal_name:Optional[str]=Field(max_length=100)
    tax_filing_name:Optional[str]=Field(max_length=100)
    business_start_date:Optional[str]
    website:Optional[str]=Field(max_length=150)
    phone_number:Optional[str]=Field(max_length=15)
    fax:Optional[str]=Field(max_length=15)
    business_license_number:Optional[str]=Field(max_length=30)
    business_license_state_id:Optional[str]=Field(max_length=2)
    rep_code:str=Field(max_length=15)
    mcc_id:Optional[int]
    business_desc:Optional[str]
    when_card_charged_id:Optional[str]=Field(max_length=15)
    services_provided_in_id:Optional[str]=Field(max_length=15)
    annual_volume:Optional[int]
    average_ticket:Optional[int]
    high_ticket:Optional[int]
    refund_policy_id:Optional[str]=Field(max_length=15)
    is_seasonal:bool
    product_delivery_id:Optional[str]=Field(max_length=15)
    in_person_pct:Optional[int]
    online_pct:Optional[int]
    telephone_pct:Optional[int]
    ownership_type:Optional[str]=Field(max_length=15)
    back_end_platform_id:Optional[str]=Field(max_length=15)
    customer_id:int
    merchant_status_id:int
    priority:bool
    created_by:int
    class Config:
        orm_mode = True
    
class MerchantUpdate(BaseModel):
    
    dba_name:str=Field(max_length=100)
    legal_name:Optional[str]=Field(max_length=100)
    tax_filing_name:Optional[str]=Field(max_length=100)
    business_start_date:Optional[str]
    website:Optional[str]=Field(max_length=150)
    phone_number:Optional[str]=Field(max_length=15)
    fax:Optional[str]=Field(max_length=15)
    business_license_number:Optional[str]=Field(max_length=30)
    business_license_state_id:Optional[str]=Field(max_length=2)
    rep_code:str=Field(max_length=15)
    mcc_id:Optional[int]
    business_desc:Optional[str]
    when_card_charged_id:Optional[str]=Field(max_length=15)
    services_provided_in_id:Optional[str]=Field(max_length=15)
    annual_volume:Optional[int]
    average_ticket:Optional[int]
    high_ticket:Optional[int]
    refund_policy_id:Optional[str]=Field(max_length=15)
    is_seasonal:bool
    product_delivery_id:Optional[str]=Field(max_length=15)
    in_person_pct:Optional[int]
    online_pct:Optional[int]
    telephone_pct:Optional[int]
    ownership_type:Optional[str]=Field(max_length=15)
    back_end_platform_id:Optional[str]=Field(max_length=15)
    customer_id:int
    merchant_status_id:int
    priority:bool
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class Ticket(BaseModel):
    
    ticket_id:int
    ticket_reason_id:int
    ticket_reason_ref:Optional[RefTicketReason]
    merchant_id:int
    merchant_ref:Optional[Merchant]
    description:str
    ticket_status_id:int
    ticket_status_ref:Optional[RefTicketStatus]
    visible_to_merchant:bool
    submitted_by:int
    assigned_to:Optional[int]
    assigned_on:Optional[datetime]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class TicketCreate(BaseModel):
    
    ticket_reason_id:int
    merchant_id:int
    description:str
    ticket_status_id:int
    visible_to_merchant:bool
    submitted_by:int
    assigned_to:Optional[int]
    #assigned_on:datetime
    created_by:int
    class Config:
        orm_mode = True
    
class TicketUpdate(BaseModel):
    
    ticket_reason_id:int
    merchant_id:int
    description:str
    ticket_status_id:int
    visible_to_merchant:bool
    submitted_by:int
    assigned_to:Optional[int]
    assigned_on:Optional[datetime]
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class Attachment(BaseModel):
    
    attachment_id:int
    merchant_id:int
    merchant_ref:Optional[Merchant]
    ticket_id:Optional[int]
    ticket_ref:Optional[Ticket]
    attachment_type_id:int
    attachment_type_ref:Optional[RefAttachmentType]
    file_pointer:str=Field(max_length=250)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class AttachmentCreate(BaseModel):
    
    merchant_id:int
    ticket_id:Optional[int]
    attachment_type_id:int
    file_pointer:str=Field(max_length=250)
    created_by:int
    class Config:
        orm_mode = True
    
class AttachmentUpdate(BaseModel):
    
    merchant_id:int
    ticket_id:Optional[int]
    attachment_type_id:int
    file_pointer:str=Field(max_length=250)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class SalesOffice(BaseModel):
    
    sales_office_id:int
    name:str=Field(max_length=30)
    branding_id:int
    branding_ref:Optional[Branding]
    address1:Optional[str]=Field(max_length=50)
    address2:Optional[str]=Field(max_length=50)
    city:Optional[str]=Field(max_length=30)
    state_id:Optional[str]=Field(max_length=2)
    state_ref:Optional[RefState]
    zip:Optional[str]=Field(max_length=5)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class SalesOfficeCreate(BaseModel):
    
    name:str=Field(max_length=30)
    branding_id:int
    address1:Optional[str]=Field(max_length=50)
    address2:Optional[str]=Field(max_length=50)
    city:Optional[str]=Field(max_length=30)
    state_id:Optional[str]=Field(max_length=2)
    zip:Optional[str]=Field(max_length=5)
    created_by:int
    class Config:
        orm_mode = True
    
class SalesOfficeUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    branding_id:int
    address1:Optional[str]=Field(max_length=50)
    address2:Optional[str]=Field(max_length=50)
    city:Optional[str]=Field(max_length=30)
    state_id:Optional[str]=Field(max_length=2)
    zip:Optional[str]=Field(max_length=5)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class SalesPerson(BaseModel):
    
    sales_person_id:int
    name:str=Field(max_length=30)
    branding_id:Optional[int]
    branding_ref:Optional[Branding]
    sales_person_type_id:int
    sales_person_type_ref:Optional[RefSalesPersonType]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class SalesPersonCreate(BaseModel):
    
    name:str=Field(max_length=30)
    branding_id:Optional[int]
    sales_person_type_id:int
    created_by:int
    class Config:
        orm_mode = True
    
class SalesPersonUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    branding_id:Optional[int]
    sales_person_type_id:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class FeeTemplate(BaseModel):
    
    fee_template_id:int
    name:str=Field(max_length=30)
    sales_office_id:int
    sales_office_ref:Optional[SalesOffice]
    sales_person_id:Optional[int]
    sales_person_ref:Optional[SalesPerson]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class FeeTemplateCreate(BaseModel):
    
    name:str=Field(max_length=30)
    sales_office_id:int
    sales_person_id:Optional[int]
    created_by:int
    class Config:
        orm_mode = True
    
class FeeTemplateUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    sales_office_id:int
    sales_person_id:Optional[int]
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class FeeTemplateDetail(BaseModel):
    
    fee_template_detail_id:int
    fee_template_id:int
    fee_template_ref:Optional[FeeTemplate]
    fee_id:int
    fee_ref:Optional[RefFee]
    price:int
    min_price:int
    max_price:int
    is_allowed:bool
    is_mutable:bool
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class FeeTemplateDetailCreate(BaseModel):
    
    fee_template_id:int
    fee_id:int
    price:int
    min_price:int
    max_price:int
    is_allowed:bool
    is_mutable:bool
    created_by:int
    class Config:
        orm_mode = True
    
class FeeTemplateDetailUpdate(BaseModel):
    
    fee_template_id:int
    fee_id:int
    price:int
    min_price:int
    max_price:int
    is_allowed:bool
    is_mutable:bool
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class MerchantAddress(BaseModel):
    
    merchant_address_id:int
    merchant_id:int
    merchant_ref:Optional[Merchant]
    address_type_id:int
    address_type_ref:Optional[RefAddressType]
    address1:str=Field(max_length=50)
    address2:Optional[str]=Field(max_length=50)
    city:str=Field(max_length=30)
    state_id:str=Field(max_length=2)
    state_ref:Optional[RefState]
    zip:str=Field(max_length=5)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class MerchantAddressCreate(BaseModel):
    
    merchant_id:int
    address_type_id:int
    address1:str=Field(max_length=50)
    address2:Optional[str]=Field(max_length=50)
    city:str=Field(max_length=30)
    state_id:str=Field(max_length=2)
    zip:str=Field(max_length=5)
    created_by:int
    class Config:
        orm_mode = True
    
class MerchantAddressUpdate(BaseModel):
    
    merchant_id:int
    address_type_id:int
    address1:str=Field(max_length=50)
    address2:Optional[str]=Field(max_length=50)
    city:str=Field(max_length=30)
    state_id:str=Field(max_length=2)
    zip:str=Field(max_length=5)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class MerchantBank(BaseModel):
    
    merchant_bank_id:int
    merchant_id:int
    merchant_ref:Optional[Merchant]
    bank_name:Optional[str]=Field(max_length=30)
    bank_account_type:str=Field(max_length=15)
    usage:str=Field(max_length=30)
    account_number_token:Optional[str]=Field(max_length=50)
    routing_number:Optional[str]=Field(max_length=25)
    voided_check_attachment_id:Optional[int]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class MerchantBankCreate(BaseModel):
    
    merchant_id:int
    bank_name:Optional[str]=Field(max_length=30)
    bank_account_type:str=Field(max_length=15)
    usage:str=Field(max_length=30)
    account_number_token:Optional[str]=Field(max_length=50)
    routing_number:Optional[str]=Field(max_length=25)
    voided_check_attachment_id:Optional[int]
    created_by:int
    class Config:
        orm_mode = True
    
class MerchantBankUpdate(BaseModel):
    
    merchant_id:int
    bank_name:Optional[str]=Field(max_length=30)
    bank_account_type:str=Field(max_length=15)
    usage:str=Field(max_length=30)
    account_number_token:Optional[str]=Field(max_length=50)
    routing_number:Optional[str]=Field(max_length=25)
    voided_check_attachment_id:Optional[int]
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class MerchantContact(BaseModel):
    
    merchant_contact_id:int
    merchant_id:int
    merchant_ref:Optional[Merchant]
    first_name:Optional[str]=Field(max_length=30)
    last_name:Optional[str]=Field(max_length=30)
    title:Optional[str]=Field(max_length=30)
    ownership_pct:Optional[int]
    phone:Optional[str]=Field(max_length=15)
    email:Optional[str]=Field(max_length=50)
    ssn_token:Optional[str]=Field(max_length=50)
    dob:Optional[str]
    dl_number:Optional[str]=Field(max_length=30)
    dl_state_id:Optional[int]
    dl_state_ref:Optional[RefState]
    res_address1:Optional[str]=Field(max_length=50)
    res_address2:Optional[str]=Field(max_length=50)
    res_city:Optional[str]=Field(max_length=30)
    res_state_id:Optional[int]
    res_state_ref:Optional[RefState]
    res_zip:Optional[str]=Field(max_length=5)
    is_owner:bool
    is_signer:bool
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class MerchantContactCreate(BaseModel):
    
    merchant_id:int
    first_name:Optional[str]=Field(max_length=30)
    last_name:Optional[str]=Field(max_length=30)
    title:Optional[str]=Field(max_length=30)
    ownership_pct:Optional[int]
    phone:Optional[str]=Field(max_length=15)
    email:Optional[str]=Field(max_length=50)
    ssn_token:Optional[str]=Field(max_length=50)
    d_o_b:Optional[str]
    dl_number:Optional[str]=Field(max_length=30)
    dl_state_id:Optional[int]
    res_address1:Optional[str]=Field(max_length=50)
    res_address2:Optional[str]=Field(max_length=50)
    res_city:Optional[str]=Field(max_length=30)
    res_state_id:Optional[int]
    res_zip:Optional[str]=Field(max_length=5)
    is_owner:bool
    is_signer:bool
    created_by:int
    class Config:
        orm_mode = True
    
class MerchantContactUpdate(BaseModel):
    
    merchant_id:int
    first_name:Optional[str]=Field(max_length=30)
    last_name:Optional[str]=Field(max_length=30)
    title:Optional[str]=Field(max_length=30)
    ownership_pct:Optional[int]
    phone:Optional[str]=Field(max_length=15)
    email:Optional[str]=Field(max_length=50)
    ssn_token:Optional[str]=Field(max_length=50)
    d_o_b:Optional[str]
    d_l_number:Optional[str]=Field(max_length=30)
    dl_state_id:Optional[int]
    res_address1:Optional[str]=Field(max_length=50)
    res_address2:Optional[str]=Field(max_length=50)
    res_city:Optional[str]=Field(max_length=30)
    res_state_id:Optional[int]
    res_zip:Optional[str]=Field(max_length=5)
    is_owner:bool
    is_signer:bool
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class MerchantFees(BaseModel):
    
    merchant_fees_id:int
    merchant_id:int
    merchant_ref:Optional[Merchant]
    fee_id:int
    fee_ref:Optional[RefFee]
    price:int
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class MerchantFeesCreate(BaseModel):
    
    merchant_id:int
    fee_id:int
    price:int
    created_by:int
    class Config:
        orm_mode = True
    
class MerchantFeesUpdate(BaseModel):
    
    merchant_id:int
    fee_id:int
    price:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class Order(BaseModel):
    
    order_id:int
    merchant_id:int
    merchant_ref:Optional[Merchant]
    total_amount:int
    order_status_id:int
    order_status_ref:Optional[RefOrderStatus]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class OrderCreate(BaseModel):
    
    merchant_id:int
    total_amount:int
    order_status_id:int
    created_by:int
    class Config:
        orm_mode = True
    
class OrderUpdate(BaseModel):
    
    merchant_id:int
    total_amount:int
    order_status_id:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class MerchantProduct(BaseModel):
    
    merchant_product_id:int
    merchant_id:int
    merchant_ref:Optional[Merchant]
    product_id:int
    product_ref:Optional[RefProduct]
    order_id:int
    order_ref:Optional[Order]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class MerchantProductCreate(BaseModel):
    
    merchant_id:int
    product_id:int
    order_id:int
    created_by:int
    class Config:
        orm_mode = True
    
class MerchantProductUpdate(BaseModel):
    
    merchant_id:int
    product_id:int
    order_id:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class OrderLine(BaseModel):
    
    order_line_id:int
    order_id:int
    order_ref:Optional[Order]
    product_id:int
    product_ref:Optional[RefProduct]
    quantity:int
    price:int
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class OrderLineCreate(BaseModel):
    
    order_id:int
    product_id:int
    quantity:int
    price:int
    created_by:int
    class Config:
        orm_mode = True
    
class OrderLineUpdate(BaseModel):
    
    order_id:int
    product_id:int
    quantity:int
    price:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class Pricing(BaseModel):
    
    pricing_id:int
    order_line_id:Optional[int]
    order_line_ref:Optional[OrderLine]
    card_type_id:int
    card_type_ref:Optional[RefCardType]
    qual_rate:float
    mid_qual_rate:float
    non_qual_rate:float
    auth_rate:float
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class PricingCreate(BaseModel):
    
    order_line_id:Optional[int]
    card_type_id:int
    qual_rate:float
    mid_qual_rate:float
    non_qual_rate:float
    auth_rate:float
    created_by:int
    class Config:
        orm_mode = True
    
class PricingUpdate(BaseModel):
    
    order_line_id:Optional[int]
    card_type_id:int
    qual_rate:float
    mid_qual_rate:float
    non_qual_rate:float
    auth_rate:float
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class ProductConfig(BaseModel):
    
    product_config_id:int
    merchant_product_id:int
    merchant_product_ref:Optional[MerchantProduct]
    config_type:int
    config_type_ref:Optional[RefConfigType]
    config:Optional[str]=Field(max_length=100)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class ProductConfigCreate(BaseModel):
    
    merchant_product_id:int
    config_type:int
    config:Optional[str]=Field(max_length=100)
    created_by:int
    class Config:
        orm_mode = True
    
class ProductConfigUpdate(BaseModel):
    
    merchant_product_id:int
    config_type:int
    config:Optional[str]=Field(max_length=100)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RepScheduleA(BaseModel):
    
    rep_schedule_a_id:int
    name:str=Field(max_length=30)
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RepScheduleACreate(BaseModel):
    
    name:str=Field(max_length=30)
    created_by:int
    class Config:
        orm_mode = True
    
class RepScheduleAUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class RepScheduleAItem(BaseModel):
    
    schedule_a_item_id:int
    schedule_a_id:int
    schedule_a_ref:Optional[RefScheduleA]
    rate:Optional[float]
    per_item:Optional[int]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class RepScheduleAItemCreate(BaseModel):
    
    schedule_a_id:int
    rate:Optional[float]
    per_item:Optional[int]
    created_by:int
    class Config:
        orm_mode = True
    
class RepScheduleAItemUpdate(BaseModel):
    
    schedule_a_id:int
    rate:Optional[float]
    per_item:Optional[int]
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class SalesPersonRep(BaseModel):
    
    sales_person_rep_id:int
    name:str=Field(max_length=30)
    sales_person_id:int
    sales_person_ref:Optional[SalesPerson]
    sales_office_id:int
    sales_office_ref:Optional[SalesOffice]
    rep_code:str=Field(max_length=15)
    rep_code_ref:Optional[RepCodeBoardingPlatform]
    split:int
    rep_schedule_a_id:Optional[int]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class SalesPersonRepCreate(BaseModel):
    
    name:str=Field(max_length=30)
    sales_person_id:int
    sales_office_id:int
    rep_code:str=Field(max_length=15)
    split:int
    rep_schedule_a_id:Optional[int]
    created_by:int
    class Config:
        orm_mode = True
    
class SalesPersonRepUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    sales_person_id:int
    sales_office_id:int
    rep_code:str=Field(max_length=15)
    split:int
    rep_schedule_a_id:Optional[int]
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class SeasonalBusiness(BaseModel):
    
    seasonal_business_id:int
    merchant_id:int
    merchant_ref:Optional[Merchant]
    month:int
    amount:int
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class SeasonalBusinessCreate(BaseModel):
    
    merchant_id:int
    month:int
    amount:int
    created_by:int
    class Config:
        orm_mode = True
    
class SeasonalBusinessUpdate(BaseModel):
    
    merchant_id:int
    month:int
    amount:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class TicketComment(BaseModel):
    
    ticket_comment_id:int
    ticket_id:int
    ticket_ref:Optional[Ticket]
    comment:str
    visible_to_merchant:bool
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class TicketCommentCreate(BaseModel):
    
    ticket_id:int
    comment:str
    visible_to_merchant:bool
    created_by:int
    class Config:
        orm_mode = True
    
class TicketCommentUpdate(BaseModel):
    
    ticket_id:int
    comment:str
    visible_to_merchant:bool
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class UserRole(BaseModel):
    
    user_role_id:int
    name:str=Field(max_length=30)
    sales_office_id:Optional[int]
    sales_office_ref:Optional[SalesOffice]
    sales_person_id:Optional[int]
    sales_person_ref:Optional[SalesPerson]
    customer_id:Optional[int]
    customer_ref:Optional[Customer]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class UserRoleCreate(BaseModel):
    
    name:str=Field(max_length=30)
    sales_office_id:Optional[int]
    sales_person_id:Optional[int]
    customer_id:Optional[int]
    created_by:int
    class Config:
        orm_mode = True
    
class UserRoleUpdate(BaseModel):
    
    name:str=Field(max_length=30)
    sales_office_id:Optional[int]
    sales_person_id:Optional[int]
    customer_id:Optional[int]
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class UserRolePermission(BaseModel):
    
    user_role_permission_id:int
    user_role_id:int
    user_role_ref:Optional[UserRole]
    permission_id:int
    permission_ref:Optional[RefPermission]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class UserRolePermissionCreate(BaseModel):
    
    user_role_id:int
    permission_id:int
    created_by:int
    class Config:
        orm_mode = True
    
class UserRolePermissionUpdate(BaseModel):
    
    user_role_id:int
    permission_id:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    

class Users(BaseModel):
    
    user_id:int
    user_name:str=Field(max_length=30)
    password:str=Field(max_length=100)
    first_name:str=Field(max_length=30)
    last_name:str=Field(max_length=30)
    email:str=Field(max_length=50)
    user_type_id:int
    user_type_ref:Optional[RefUserType]
    sales_office_id:Optional[int]
    sales_office_ref:Optional[SalesOffice]
    sales_person_id:Optional[int]
    sales_person_ref:Optional[SalesPerson]
    customer_id:Optional[int]
    customer_ref:Optional[Customer]
    user_role_id:int
    user_role_ref:Optional[UserRole]
    created_on:Optional[datetime]
    modified_on:Optional[datetime]
    created_by:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True

    
class UsersCreate(BaseModel):
    
    user_name:str=Field(max_length=30)
    password:str=Field(max_length=100)
    first_name:str=Field(max_length=30)
    last_name:str=Field(max_length=30)
    email:str=Field(max_length=50)
    user_type_id:int
    sales_office_id:Optional[int]
    sales_person_id:Optional[int]
    customer_id:Optional[int]
    user_role_id:int
    created_by:int
    class Config:
        orm_mode = True
    
class UsersUpdate(BaseModel):
    
    user_name:str=Field(max_length=30)
    password:str=Field(max_length=100)
    first_name:str=Field(max_length=30)
    last_name:str=Field(max_length=30)
    email:str=Field(max_length=50)
    user_type_id:int
    sales_office_id:Optional[int]
    sales_person_id:Optional[int]
    customer_id:Optional[int]
    user_role_id:int
    modified_by:Optional[int]
    class Config:
        orm_mode = True
    