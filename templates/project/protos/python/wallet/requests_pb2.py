# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: wallet/requests.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="wallet/requests.proto",
    package="qbit.wallet",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=_b(
        '\n\x15wallet/requests.proto\x12\x0bqbit.wallet":\n\x10GetStatusRequest\x12\x11\n\twallet_id\x18\x01 \x01(\t\x12\x13\n\x0bsdk_version\x18\x02 \x01(\t">\n\x13\x41uthenticateRequest\x12\x14\n\x0cphone_number\x18\x01 \x01(\t\x12\x11\n\tunique_id\x18\x02 \x01(\t":\n\x19VerifyAuthenticateRequest\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x0f\n\x07raw_otp\x18\x02 \x01(\t"?\n\x1bSetWalletPermissionsRequest\x12\x11\n\twallet_id\x18\x01 \x01(\t\x12\r\n\x05grant\x18\x02 \x01(\x08"\'\n\x11GetPartnerRequest\x12\x12\n\npartner_id\x18\x01 \x01(\t"/\n\x19GetPartnerServicesRequest\x12\x12\n\npartner_id\x18\x01 \x01(\t",\n\x16GetPartnerDebtsRequest\x12\x12\n\npartner_id\x18\x01 \x01(\t"f\n\x1b\x43reateWalletPaymentsRequest\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x12\n\nservice_id\x18\x02 \x01(\t\x12\x11\n\twallet_id\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x05"\'\n\x11GetPaymentRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t"*\n\x14\x43\x61ncelPaymentRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t"e\n\x14ModifyPaymentRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x05\x12\x17\n\x0fprevious_amount\x18\x04 \x01(\x05"L\n\x14VerifyPaymentRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x05"3\n\x1dGetPaymentTransactionsRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t"%\n\x10GetWalletRequest\x12\x11\n\twallet_id\x18\x01 \x01(\t"-\n\x18GetWalletPaymentsRequest\x12\x11\n\twallet_id\x18\x01 \x01(\t"*\n\x15GetWalletDebtsRequest\x12\x11\n\twallet_id\x18\x01 \x01(\tb\x06proto3'
    ),
)


_GETSTATUSREQUEST = _descriptor.Descriptor(
    name="GetStatusRequest",
    full_name="qbit.wallet.GetStatusRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="wallet_id",
            full_name="qbit.wallet.GetStatusRequest.wallet_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="sdk_version",
            full_name="qbit.wallet.GetStatusRequest.sdk_version",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=38,
    serialized_end=96,
)


_AUTHENTICATEREQUEST = _descriptor.Descriptor(
    name="AuthenticateRequest",
    full_name="qbit.wallet.AuthenticateRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="phone_number",
            full_name="qbit.wallet.AuthenticateRequest.phone_number",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="unique_id",
            full_name="qbit.wallet.AuthenticateRequest.unique_id",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=98,
    serialized_end=160,
)


_VERIFYAUTHENTICATEREQUEST = _descriptor.Descriptor(
    name="VerifyAuthenticateRequest",
    full_name="qbit.wallet.VerifyAuthenticateRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="hash",
            full_name="qbit.wallet.VerifyAuthenticateRequest.hash",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="raw_otp",
            full_name="qbit.wallet.VerifyAuthenticateRequest.raw_otp",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=162,
    serialized_end=220,
)


_SETWALLETPERMISSIONSREQUEST = _descriptor.Descriptor(
    name="SetWalletPermissionsRequest",
    full_name="qbit.wallet.SetWalletPermissionsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="wallet_id",
            full_name="qbit.wallet.SetWalletPermissionsRequest.wallet_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="grant",
            full_name="qbit.wallet.SetWalletPermissionsRequest.grant",
            index=1,
            number=2,
            type=8,
            cpp_type=7,
            label=1,
            has_default_value=False,
            default_value=False,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=222,
    serialized_end=285,
)


_GETPARTNERREQUEST = _descriptor.Descriptor(
    name="GetPartnerRequest",
    full_name="qbit.wallet.GetPartnerRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="partner_id",
            full_name="qbit.wallet.GetPartnerRequest.partner_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=287,
    serialized_end=326,
)


_GETPARTNERSERVICESREQUEST = _descriptor.Descriptor(
    name="GetPartnerServicesRequest",
    full_name="qbit.wallet.GetPartnerServicesRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="partner_id",
            full_name="qbit.wallet.GetPartnerServicesRequest.partner_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=328,
    serialized_end=375,
)


_GETPARTNERDEBTSREQUEST = _descriptor.Descriptor(
    name="GetPartnerDebtsRequest",
    full_name="qbit.wallet.GetPartnerDebtsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="partner_id",
            full_name="qbit.wallet.GetPartnerDebtsRequest.partner_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=377,
    serialized_end=421,
)


_CREATEWALLETPAYMENTSREQUEST = _descriptor.Descriptor(
    name="CreateWalletPaymentsRequest",
    full_name="qbit.wallet.CreateWalletPaymentsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="order_id",
            full_name="qbit.wallet.CreateWalletPaymentsRequest.order_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="service_id",
            full_name="qbit.wallet.CreateWalletPaymentsRequest.service_id",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="wallet_id",
            full_name="qbit.wallet.CreateWalletPaymentsRequest.wallet_id",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="amount",
            full_name="qbit.wallet.CreateWalletPaymentsRequest.amount",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=423,
    serialized_end=525,
)


_GETPAYMENTREQUEST = _descriptor.Descriptor(
    name="GetPaymentRequest",
    full_name="qbit.wallet.GetPaymentRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="payment_id",
            full_name="qbit.wallet.GetPaymentRequest.payment_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=527,
    serialized_end=566,
)


_CANCELPAYMENTREQUEST = _descriptor.Descriptor(
    name="CancelPaymentRequest",
    full_name="qbit.wallet.CancelPaymentRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="payment_id",
            full_name="qbit.wallet.CancelPaymentRequest.payment_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=568,
    serialized_end=610,
)


_MODIFYPAYMENTREQUEST = _descriptor.Descriptor(
    name="ModifyPaymentRequest",
    full_name="qbit.wallet.ModifyPaymentRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="payment_id",
            full_name="qbit.wallet.ModifyPaymentRequest.payment_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="order_id",
            full_name="qbit.wallet.ModifyPaymentRequest.order_id",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="amount",
            full_name="qbit.wallet.ModifyPaymentRequest.amount",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="previous_amount",
            full_name="qbit.wallet.ModifyPaymentRequest.previous_amount",
            index=3,
            number=4,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=612,
    serialized_end=713,
)


_VERIFYPAYMENTREQUEST = _descriptor.Descriptor(
    name="VerifyPaymentRequest",
    full_name="qbit.wallet.VerifyPaymentRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="payment_id",
            full_name="qbit.wallet.VerifyPaymentRequest.payment_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="order_id",
            full_name="qbit.wallet.VerifyPaymentRequest.order_id",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="amount",
            full_name="qbit.wallet.VerifyPaymentRequest.amount",
            index=2,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=715,
    serialized_end=791,
)


_GETPAYMENTTRANSACTIONSREQUEST = _descriptor.Descriptor(
    name="GetPaymentTransactionsRequest",
    full_name="qbit.wallet.GetPaymentTransactionsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="payment_id",
            full_name="qbit.wallet.GetPaymentTransactionsRequest.payment_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=793,
    serialized_end=844,
)


_GETWALLETREQUEST = _descriptor.Descriptor(
    name="GetWalletRequest",
    full_name="qbit.wallet.GetWalletRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="wallet_id",
            full_name="qbit.wallet.GetWalletRequest.wallet_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=846,
    serialized_end=883,
)


_GETWALLETPAYMENTSREQUEST = _descriptor.Descriptor(
    name="GetWalletPaymentsRequest",
    full_name="qbit.wallet.GetWalletPaymentsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="wallet_id",
            full_name="qbit.wallet.GetWalletPaymentsRequest.wallet_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=885,
    serialized_end=930,
)


_GETWALLETDEBTSREQUEST = _descriptor.Descriptor(
    name="GetWalletDebtsRequest",
    full_name="qbit.wallet.GetWalletDebtsRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="wallet_id",
            full_name="qbit.wallet.GetWalletDebtsRequest.wallet_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=932,
    serialized_end=974,
)

DESCRIPTOR.message_types_by_name["GetStatusRequest"] = _GETSTATUSREQUEST
DESCRIPTOR.message_types_by_name["AuthenticateRequest"] = _AUTHENTICATEREQUEST
DESCRIPTOR.message_types_by_name[
    "VerifyAuthenticateRequest"
] = _VERIFYAUTHENTICATEREQUEST
DESCRIPTOR.message_types_by_name[
    "SetWalletPermissionsRequest"
] = _SETWALLETPERMISSIONSREQUEST
DESCRIPTOR.message_types_by_name["GetPartnerRequest"] = _GETPARTNERREQUEST
DESCRIPTOR.message_types_by_name[
    "GetPartnerServicesRequest"
] = _GETPARTNERSERVICESREQUEST
DESCRIPTOR.message_types_by_name["GetPartnerDebtsRequest"] = _GETPARTNERDEBTSREQUEST
DESCRIPTOR.message_types_by_name[
    "CreateWalletPaymentsRequest"
] = _CREATEWALLETPAYMENTSREQUEST
DESCRIPTOR.message_types_by_name["GetPaymentRequest"] = _GETPAYMENTREQUEST
DESCRIPTOR.message_types_by_name["CancelPaymentRequest"] = _CANCELPAYMENTREQUEST
DESCRIPTOR.message_types_by_name["ModifyPaymentRequest"] = _MODIFYPAYMENTREQUEST
DESCRIPTOR.message_types_by_name["VerifyPaymentRequest"] = _VERIFYPAYMENTREQUEST
DESCRIPTOR.message_types_by_name[
    "GetPaymentTransactionsRequest"
] = _GETPAYMENTTRANSACTIONSREQUEST
DESCRIPTOR.message_types_by_name["GetWalletRequest"] = _GETWALLETREQUEST
DESCRIPTOR.message_types_by_name["GetWalletPaymentsRequest"] = _GETWALLETPAYMENTSREQUEST
DESCRIPTOR.message_types_by_name["GetWalletDebtsRequest"] = _GETWALLETDEBTSREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetStatusRequest = _reflection.GeneratedProtocolMessageType(
    "GetStatusRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETSTATUSREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.GetStatusRequest)
    },
)
_sym_db.RegisterMessage(GetStatusRequest)

AuthenticateRequest = _reflection.GeneratedProtocolMessageType(
    "AuthenticateRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUTHENTICATEREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.AuthenticateRequest)
    },
)
_sym_db.RegisterMessage(AuthenticateRequest)

VerifyAuthenticateRequest = _reflection.GeneratedProtocolMessageType(
    "VerifyAuthenticateRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _VERIFYAUTHENTICATEREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.VerifyAuthenticateRequest)
    },
)
_sym_db.RegisterMessage(VerifyAuthenticateRequest)

SetWalletPermissionsRequest = _reflection.GeneratedProtocolMessageType(
    "SetWalletPermissionsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _SETWALLETPERMISSIONSREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.SetWalletPermissionsRequest)
    },
)
_sym_db.RegisterMessage(SetWalletPermissionsRequest)

GetPartnerRequest = _reflection.GeneratedProtocolMessageType(
    "GetPartnerRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPARTNERREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.GetPartnerRequest)
    },
)
_sym_db.RegisterMessage(GetPartnerRequest)

GetPartnerServicesRequest = _reflection.GeneratedProtocolMessageType(
    "GetPartnerServicesRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPARTNERSERVICESREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.GetPartnerServicesRequest)
    },
)
_sym_db.RegisterMessage(GetPartnerServicesRequest)

GetPartnerDebtsRequest = _reflection.GeneratedProtocolMessageType(
    "GetPartnerDebtsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPARTNERDEBTSREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.GetPartnerDebtsRequest)
    },
)
_sym_db.RegisterMessage(GetPartnerDebtsRequest)

CreateWalletPaymentsRequest = _reflection.GeneratedProtocolMessageType(
    "CreateWalletPaymentsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CREATEWALLETPAYMENTSREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.CreateWalletPaymentsRequest)
    },
)
_sym_db.RegisterMessage(CreateWalletPaymentsRequest)

GetPaymentRequest = _reflection.GeneratedProtocolMessageType(
    "GetPaymentRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPAYMENTREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.GetPaymentRequest)
    },
)
_sym_db.RegisterMessage(GetPaymentRequest)

CancelPaymentRequest = _reflection.GeneratedProtocolMessageType(
    "CancelPaymentRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _CANCELPAYMENTREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.CancelPaymentRequest)
    },
)
_sym_db.RegisterMessage(CancelPaymentRequest)

ModifyPaymentRequest = _reflection.GeneratedProtocolMessageType(
    "ModifyPaymentRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _MODIFYPAYMENTREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.ModifyPaymentRequest)
    },
)
_sym_db.RegisterMessage(ModifyPaymentRequest)

VerifyPaymentRequest = _reflection.GeneratedProtocolMessageType(
    "VerifyPaymentRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _VERIFYPAYMENTREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.VerifyPaymentRequest)
    },
)
_sym_db.RegisterMessage(VerifyPaymentRequest)

GetPaymentTransactionsRequest = _reflection.GeneratedProtocolMessageType(
    "GetPaymentTransactionsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETPAYMENTTRANSACTIONSREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.GetPaymentTransactionsRequest)
    },
)
_sym_db.RegisterMessage(GetPaymentTransactionsRequest)

GetWalletRequest = _reflection.GeneratedProtocolMessageType(
    "GetWalletRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETWALLETREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.GetWalletRequest)
    },
)
_sym_db.RegisterMessage(GetWalletRequest)

GetWalletPaymentsRequest = _reflection.GeneratedProtocolMessageType(
    "GetWalletPaymentsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETWALLETPAYMENTSREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.GetWalletPaymentsRequest)
    },
)
_sym_db.RegisterMessage(GetWalletPaymentsRequest)

GetWalletDebtsRequest = _reflection.GeneratedProtocolMessageType(
    "GetWalletDebtsRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETWALLETDEBTSREQUEST,
        "__module__": "wallet.requests_pb2"
        # @@protoc_insertion_point(class_scope:qbit.wallet.GetWalletDebtsRequest)
    },
)
_sym_db.RegisterMessage(GetWalletDebtsRequest)


# @@protoc_insertion_point(module_scope)