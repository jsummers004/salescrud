from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text, DateTime, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.sql import func


class RefOrderStatusModel(Base):
    __tablename__ = "ref_order_status"
    order_status_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefRefundPolicyModel(Base):
    __tablename__ = "ref_refund_policy"
    refund_policy_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefProductDeliveryModel(Base):
    __tablename__ = "ref_product_delivery"
    product_delivery_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefOwnershipTypeModel(Base):
    __tablename__ = "ref_ownership_type"
    ownership_type_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefMerchantStatusModel(Base):
    __tablename__ = "ref_merchant_status"
    merchant_status_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefPermissionModel(Base):
    __tablename__ = "ref_permission"
    permission_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefTicketStatusModel(Base):
    __tablename__ = "ref_ticket_status"
    ticket_status_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefFeeModel(Base):
    __tablename__ = "ref_fee"
    fee_id=Column(Integer,primary_key=True,nullable=False)
    
    fee_category=Column(Integer,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefAddressTypeModel(Base):
    __tablename__ = "ref_address_type"
    address_type_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefTicketReasonModel(Base):
    __tablename__ = "ref_ticket_reason"
    ticket_reason_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class MerchantBoardingPlatformModel(Base):
    __tablename__ = "merchant_boarding_platform"
    mbp_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefBackEndPlatformModel(Base):
    __tablename__ = "ref_back_end_platform"
    back_end_platform_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefMbpBackEndModel(Base):
    __tablename__ = "ref_mbp_back_end"
    mbp_back_end_id=Column(Integer,primary_key=True,nullable=False)
    
    mbp_id=Column(Integer,ForeignKey("merchant_boarding_platform.mbp_id"),nullable=False)
    
    mbp_ref=relationship(MerchantBoardingPlatformModel)
    back_end_platform_id=Column(Integer,ForeignKey("ref_back_end_platform.back_end_platform_id"),nullable=False)
    
    back_end_platform_ref=relationship(RefBackEndPlatformModel)
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefConfigTypeModel(Base):
    __tablename__ = "ref_config_type"
    config_type_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefProductTypeModel(Base):
    __tablename__ = "ref_product_type"
    product_type_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefProductModel(Base):
    __tablename__ = "ref_product"
    product_id=Column(Integer,primary_key=True,nullable=False)
    
    product_type_id=Column(Integer,ForeignKey("ref_product_type.product_type_id"),nullable=False)
    
    product_type_ref=relationship(RefProductTypeModel)
    name=Column(String(30),nullable=False)
    
    image=Column(String(250))
    
    description=Column(Text)
    
    features=Column(Text)
    
    default_price=Column(Integer)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefScheduleAModel(Base):
    __tablename__ = "ref_schedule_a"
    schedule_a_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(100),nullable=False)
    
    cost_type=Column(String(15),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefProcessorModel(Base):
    __tablename__ = "ref_processor"
    processor_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefScheduleAMapModel(Base):
    __tablename__ = "ref_schedule_a_map"
    schedule_a_map_id=Column(Integer,primary_key=True,nullable=False)
    
    schedule_a_id=Column(Integer,ForeignKey("ref_schedule_a.schedule_a_id"),nullable=False)
    
    schedule_a_ref=relationship(RefScheduleAModel)
    processor_id=Column(Integer,ForeignKey("ref_processor.processor_id"),nullable=False)
    
    processor_ref=relationship(RefProcessorModel)
    fee_code=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefCardTypeModel(Base):
    __tablename__ = "ref_card_type"
    card_type_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefAttachmentTypeModel(Base):
    __tablename__ = "ref_attachment_type"
    attachment_type_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(50),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefStateModel(Base):
    __tablename__ = "ref_state"
    state_id=Column(Integer,primary_key=True,nullable=False)
    state_code=Column(String(2), unique=True)
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefUserTypeModel(Base):
    __tablename__ = "ref_user_type"
    user_type_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefSalesPersonTypeModel(Base):
    __tablename__ = "ref_sales_person_type"
    sales_person_type_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefMccModel(Base):
    __tablename__ = "ref_mcc"
    mcc_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(255),nullable=False)
    
    mcc_code=Column(String(15),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefWhenCardChargedModel(Base):
    __tablename__ = "ref_when_card_charged"
    when_card_charged_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(50),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RefServicesProvidedInModel(Base):
    __tablename__ = "ref_services_provided_in"
    services_provided_in_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RepCodeBoardingPlatformModel(Base):
    __tablename__ = "rep_code_boarding_platform"
    rep_code_boarding_platform_id=Column(Integer,primary_key=True,nullable=False)
    
    rep_code=Column(String(15),unique=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    mbp_id=Column(Integer,ForeignKey("merchant_boarding_platform.mbp_id"),nullable=False)
    
    mbp_ref=relationship(MerchantBoardingPlatformModel)
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class BrandingModel(Base):
    __tablename__ = "branding"
    branding_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    logo=Column(String(200))
    
    contact_phone=Column(String(15),nullable=False)
    
    contact_email=Column(String(50),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class CustomerModel(Base):
    __tablename__ = "customer"
    customer_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    branding_id=Column(Integer,ForeignKey("branding.branding_id"))
    
    branding_ref=relationship(BrandingModel)
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class MerchantModel(Base):
    __tablename__ = "merchant"
    merchant_id=Column(Integer,primary_key=True,nullable=False)
    
    dba_name=Column(String(100),nullable=False)
    
    legal_name=Column(String(100))
    
    tax_filing_name=Column(String(100))
    tax_id_token=Column(String(100))
    business_start_date=Column(String(8))
    
    website=Column(String(150))
    
    phone_number=Column(String(15))
    
    fax=Column(String(15))
    
    business_license_number=Column(String(30))
    
    business_license_state_id=Column(Integer,ForeignKey("ref_state.state_id"))
    
    business_license_state_ref=relationship(RefStateModel)
    rep_code=Column(String(15),ForeignKey("rep_code_boarding_platform.rep_code"),nullable=False)
    
    rep_code_ref=relationship(RepCodeBoardingPlatformModel)
    mcc_id=Column(Integer,ForeignKey("ref_mcc.mcc_id"))
    
    mcc_ref=relationship(RefMccModel)
    business_desc=Column(Text)
    
    when_card_charged_id=Column(Integer,ForeignKey("ref_when_card_charged.when_card_charged_id"))
    
    when_card_charged_ref=relationship(RefWhenCardChargedModel)
    services_provided_in_id=Column(Integer,ForeignKey("ref_services_provided_in.services_provided_in_id"))
    
    services_provided_in_ref=relationship(RefServicesProvidedInModel)
    annual_volume=Column(Integer)
    
    average_ticket=Column(Integer)
    
    high_ticket=Column(Integer)
    
    refund_policy_id=Column(Integer,ForeignKey("ref_refund_policy.refund_policy_id"))
    
    refund_policy_ref=relationship(RefRefundPolicyModel)
    is_seasonal=Column(Boolean,default=False,nullable=False)
    
    product_delivery_id=Column(Integer,ForeignKey("ref_product_delivery.product_delivery_id"))
    
    product_delivery_ref=relationship(RefProductDeliveryModel)
    in_person_pct=Column(Integer)
    
    online_pct=Column(Integer)
    
    telephone_pct=Column(Integer)
    
    ownership_type=Column(Integer,ForeignKey("ref_ownership_type.ownership_type_id"))
    
    ownership_type_ref=relationship(RefOwnershipTypeModel)
    back_end_platform_id=Column(Integer,ForeignKey("ref_back_end_platform.back_end_platform_id"))
    
    back_end_platform_ref=relationship(RefBackEndPlatformModel)
    customer_id=Column(Integer,ForeignKey("customer.customer_id"),nullable=False)
    
    customer_ref=relationship(CustomerModel)
    merchant_status_id=Column(Integer,ForeignKey("ref_merchant_status.merchant_status_id"),nullable=False)
    
    merchant_status_ref=relationship(RefMerchantStatusModel)
    priority=Column(Boolean,default=False,nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class TicketModel(Base):
    __tablename__ = "ticket"
    ticket_id=Column(Integer,primary_key=True,nullable=False)
    
    ticket_reason_id=Column(Integer,ForeignKey("ref_ticket_reason.ticket_reason_id"),nullable=False)
    
    ticket_reason_ref=relationship(RefTicketReasonModel)
    merchant_id=Column(Integer,ForeignKey("merchant.merchant_id"),nullable=False)
    
    merchant_ref=relationship(MerchantModel)
    description=Column(Text,nullable=False)
    
    ticket_status_id=Column(Integer,ForeignKey("ref_ticket_status.ticket_status_id"),nullable=False)
    
    ticket_status_ref=relationship(RefTicketStatusModel)
    visible_to_merchant=Column(Boolean,default=False,nullable=False)
    
    submitted_by=Column(Integer,nullable=False)
    
    assigned_to=Column(Integer)
    
    assigned_on=Column(DateTime,nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class AttachmentModel(Base):
    __tablename__ = "attachment"
    attachment_id=Column(Integer,primary_key=True,nullable=False)
    
    merchant_id=Column(Integer,ForeignKey("merchant.merchant_id"),nullable=False)
    
    merchant_ref=relationship(MerchantModel)
    ticket_id=Column(Integer,ForeignKey("ticket.ticket_id"))
    
    ticket_ref=relationship(TicketModel)
    attachment_type_id=Column(Integer,ForeignKey("ref_attachment_type.attachment_type_id"),nullable=False)
    
    attachment_type_ref=relationship(RefAttachmentTypeModel)
    file_pointer=Column(String(250),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class SalesOfficeModel(Base):
    __tablename__ = "sales_office"
    sales_office_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    branding_id=Column(Integer,ForeignKey("branding.branding_id"),nullable=False)
    
    branding_ref=relationship(BrandingModel)
    address1=Column(String(50))
    
    address2=Column(String(50))
    
    city=Column(String(30))
    
    state_id=Column(Integer,ForeignKey("ref_state.state_id"))
    
    state_ref=relationship(RefStateModel)
    zip=Column(String(5))
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class SalesPersonModel(Base):
    __tablename__ = "sales_person"
    sales_person_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    branding_id=Column(Integer,ForeignKey("branding.branding_id"))
    
    branding_ref=relationship(BrandingModel)
    sales_person_type_id=Column(Integer,ForeignKey("ref_sales_person_type.sales_person_type_id"),nullable=False)
    
    sales_person_type_ref=relationship(RefSalesPersonTypeModel)
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class FeeTemplateModel(Base):
    __tablename__ = "fee_template"
    fee_template_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    sales_office_id=Column(Integer,ForeignKey("sales_office.sales_office_id"),nullable=False)
    
    sales_office_ref=relationship(SalesOfficeModel)
    sales_person_id=Column(Integer,ForeignKey("sales_person.sales_person_id"))
    
    sales_person_ref=relationship(SalesPersonModel)
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class FeeTemplateDetailModel(Base):
    __tablename__ = "fee_template_detail"
    fee_template_detail_id=Column(Integer,primary_key=True,nullable=False)
    
    fee_template_id=Column(Integer,ForeignKey("fee_template.fee_template_id"),nullable=False)
    
    fee_template_ref=relationship(FeeTemplateModel)
    fee_id=Column(Integer,ForeignKey("ref_fee.fee_id"),nullable=False)
    
    fee_ref=relationship(RefFeeModel)
    price=Column(Integer,nullable=False)
    
    min_price=Column(Integer,nullable=False)
    
    max_price=Column(Integer,nullable=False)
    
    is_allowed=Column(Boolean,default=False,nullable=False)
    
    is_mutable=Column(Boolean,default=False,nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class MerchantAddressModel(Base):
    __tablename__ = "merchant_address"
    merchant_address_id=Column(Integer,primary_key=True,nullable=False)
    
    merchant_id=Column(Integer,ForeignKey("merchant.merchant_id"),nullable=False)
    
    merchant_ref=relationship(MerchantModel)
    address_type_id=Column(Integer,ForeignKey("ref_address_type.address_type_id"),nullable=False)
    
    address_type_ref=relationship(RefAddressTypeModel)
    address1=Column(String(50),nullable=False)
    
    address2=Column(String(50))
    
    city=Column(String(30),nullable=False)
    
    state_id=Column(Integer,ForeignKey("ref_state.state_id"),nullable=False)
    
    state_ref=relationship(RefStateModel)
    zip=Column(String(5),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class MerchantBankModel(Base):
    __tablename__ = "merchant_bank"
    merchant_bank_id=Column(Integer,primary_key=True,nullable=False)
    
    merchant_id=Column(Integer,ForeignKey("merchant.merchant_id"),nullable=False)
    
    merchant_ref=relationship(MerchantModel)
    bank_name=Column(String(30))
    
    bank_account_type=Column(Integer,nullable=False)
    
    usage=Column(String(30),nullable=False)
    
    account_number_token=Column(String(50))
    
    routing_number=Column(String(25))
    
    voided_check_attachment_id=Column(Integer)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class MerchantContactModel(Base):
    __tablename__ = "merchant_contact"
    merchant_contact_id=Column(Integer,primary_key=True,nullable=False)
    
    merchant_id=Column(Integer,ForeignKey("merchant.merchant_id"),nullable=False)
    
    merchant_ref=relationship(MerchantModel)
    first_name=Column(String(30))
    
    last_name=Column(String(30))
    
    title=Column(String(30))
    
    ownership_pct=Column(Integer)
    
    phone=Column(String(15))
    
    email=Column(String(50))
    
    ssn_token=Column(String(50))
    
    dob=Column(Date)
    
    dl_number=Column(String(30))
    
    dl_state_id=Column(Integer,ForeignKey("ref_state.state_id"))
    
    dl_state_ref=relationship(RefStateModel)
    res_address1=Column(String(50))
    
    res_address2=Column(String(50))
    
    res_city=Column(String(30))
    
    # TODO, figure out why there cannot be two FK dl_state_ref, res_state_ref

    #res_state_id=Column(Integer,ForeignKey("ref_state.state_id"))
    
    #res_state_ref=relationship(RefStateModel)
    res_zip=Column(String(5))
    
    is_owner=Column(Boolean,default=False,nullable=False)
    
    is_signer=Column(Boolean,default=False,nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class MerchantFeesModel(Base):
    __tablename__ = "merchant_fees"
    merchant_fees_id=Column(Integer,primary_key=True,nullable=False)
    
    merchant_id=Column(Integer,ForeignKey("merchant.merchant_id"),nullable=False)
    
    merchant_ref=relationship(MerchantModel)
    fee_id=Column(Integer,ForeignKey("ref_fee.fee_id"),nullable=False)
    
    fee_ref=relationship(RefFeeModel)
    price=Column(Integer,nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class OrderModel(Base):
    __tablename__ = "order"
    order_id=Column(Integer,primary_key=True,nullable=False)
    
    merchant_id=Column(Integer,ForeignKey("merchant.merchant_id"),nullable=False)
    
    merchant_ref=relationship(MerchantModel)
    total_amount=Column(Integer,nullable=False)
    
    order_status_id=Column(Integer,ForeignKey("ref_order_status.order_status_id"),nullable=False)
    
    order_status_ref=relationship(RefOrderStatusModel)
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class MerchantProductModel(Base):
    __tablename__ = "merchant_product"
    merchant_product_id=Column(Integer,primary_key=True,nullable=False)
    
    merchant_id=Column(Integer,ForeignKey("merchant.merchant_id"),nullable=False)
    
    merchant_ref=relationship(MerchantModel)
    product_id=Column(Integer,ForeignKey("ref_product.product_id"),nullable=False)
    
    product_ref=relationship(RefProductModel)
    order_id=Column(Integer,ForeignKey("order.order_id"),nullable=False)
    
    order_ref=relationship(OrderModel)
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class OrderLineModel(Base):
    __tablename__ = "order_line"
    order_line_id=Column(Integer,primary_key=True,nullable=False)
    
    order_id=Column(Integer,ForeignKey("order.order_id"),nullable=False)
    
    order_ref=relationship(OrderModel)
    product_id=Column(Integer,ForeignKey("ref_product.product_id"),nullable=False)
    
    product_ref=relationship(RefProductModel)
    quantity=Column(Integer,nullable=False)
    
    price=Column(Integer,nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class PricingModel(Base):
    __tablename__ = "pricing"
    pricing_id=Column(Integer,primary_key=True,nullable=False)
    
    order_line_id=Column(Integer,ForeignKey("order_line.order_line_id"))
    
    order_line_ref=relationship(OrderLineModel)
    card_type_id=Column(Integer,ForeignKey("ref_card_type.card_type_id"),nullable=False)
    
    card_type_ref=relationship(RefCardTypeModel)
    qual_rate=Column(Numeric,nullable=False)
    
    mid_qual_rate=Column(Numeric,nullable=False)
    
    non_qual_rate=Column(Numeric,nullable=False)
    
    auth_rate=Column(Numeric,nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class ProductConfigModel(Base):
    __tablename__ = "product_config"
    product_config_id=Column(Integer,primary_key=True,nullable=False)
    
    merchant_product_id=Column(Integer,ForeignKey("merchant_product.merchant_product_id"),nullable=False)
    
    merchant_product_ref=relationship(MerchantProductModel)
    config_type=Column(Integer,ForeignKey("ref_config_type.config_type_id"),nullable=False)
    
    config_type_ref=relationship(RefConfigTypeModel)
    config=Column(String(100))
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RepScheduleAModel(Base):
    __tablename__ = "rep_schedule_a"
    rep_schedule_a_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class RepScheduleAItemModel(Base):
    __tablename__ = "rep_schedule_a_item"
    schedule_a_item_id=Column(Integer,primary_key=True,nullable=False)
    
    schedule_a_id=Column(Integer,ForeignKey("ref_schedule_a.schedule_a_id"),nullable=False)
    
    schedule_a_ref=relationship(RefScheduleAModel)
    rate=Column(Numeric)
    
    per_item=Column(Integer)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class SalesPersonRepModel(Base):
    __tablename__ = "sales_person_rep"
    sales_person_rep_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    sales_person_id=Column(Integer,ForeignKey("sales_person.sales_person_id"),nullable=False)
    
    sales_person_ref=relationship(SalesPersonModel)
    sales_office_id=Column(Integer,ForeignKey("sales_office.sales_office_id"),nullable=False)
    
    sales_office_ref=relationship(SalesOfficeModel)
    rep_code=Column(String(15),ForeignKey("rep_code_boarding_platform.rep_code"),nullable=False)
    
    rep_code_ref=relationship(RepCodeBoardingPlatformModel)
    split=Column(Integer,nullable=False)
    
    rep_schedule_a_id=Column(Integer)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class SeasonalBusinessModel(Base):
    __tablename__ = "seasonal_business"
    seasonal_business_id=Column(Integer,primary_key=True,nullable=False)
    
    merchant_id=Column(Integer,ForeignKey("merchant.merchant_id"),nullable=False)
    
    merchant_ref=relationship(MerchantModel)
    month=Column(Integer,nullable=False)
    
    amount=Column(Integer,nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class TicketCommentModel(Base):
    __tablename__ = "ticket_comment"
    ticket_comment_id=Column(Integer,primary_key=True,nullable=False)
    
    ticket_id=Column(Integer,ForeignKey("ticket.ticket_id"),nullable=False)
    
    ticket_ref=relationship(TicketModel)
    comment=Column(Text,nullable=False)
    
    visible_to_merchant=Column(Boolean,default=False,nullable=False)
    
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class UserRoleModel(Base):
    __tablename__ = "user_role"
    user_role_id=Column(Integer,primary_key=True,nullable=False)
    
    name=Column(String(30),nullable=False)
    
    sales_office_id=Column(Integer,ForeignKey("sales_office.sales_office_id"))
    
    sales_office_ref=relationship(SalesOfficeModel)
    sales_person_id=Column(Integer,ForeignKey("sales_person.sales_person_id"))
    
    sales_person_ref=relationship(SalesPersonModel)
    customer_id=Column(Integer,ForeignKey("customer.customer_id"))
    
    customer_ref=relationship(CustomerModel)
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class UserRolePermissionModel(Base):
    __tablename__ = "user_role_permission"
    user_role_permission_id=Column(Integer,primary_key=True,nullable=False)
    
    user_role_id=Column(Integer,ForeignKey("user_role.user_role_id"),nullable=False)
    
    user_role_ref=relationship(UserRoleModel)
    permission_id=Column(Integer,ForeignKey("ref_permission.permission_id"),nullable=False)
    
    permission_ref=relationship(RefPermissionModel)
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    

class UsersModel(Base):
    __tablename__ = "users"
    user_id=Column(Integer,primary_key=True,nullable=False)
    
    user_name=Column(String(30),nullable=False)
    
    password=Column(String(100),nullable=False)
    
    first_name=Column(String(30),nullable=False)
    
    last_name=Column(String(30),nullable=False)
    
    email=Column(String(50),nullable=False)
    
    user_type_id=Column(Integer,ForeignKey("ref_user_type.user_type_id"),nullable=False)
    
    # TODO figure out how to lazy load FK data

    user_type_ref=relationship(RefUserTypeModel, lazy='select')
    sales_office_id=Column(Integer,ForeignKey("sales_office.sales_office_id"))
    
    sales_office_ref=relationship(SalesOfficeModel)
    sales_person_id=Column(Integer,ForeignKey("sales_person.sales_person_id"))
    
    sales_person_ref=relationship(SalesPersonModel)
    customer_id=Column(Integer,ForeignKey("customer.customer_id"))
    
    customer_ref=relationship(CustomerModel)
    user_role_id=Column(Integer,ForeignKey("user_role.user_role_id"),nullable=False)
    
    user_role_ref=relationship(UserRoleModel)
    created_on=Column(DateTime,nullable=False,server_default=func.now())
    
    modified_on=Column(DateTime)
    
    created_by=Column(Integer,nullable=False)
    
    modified_by=Column(Integer)
    