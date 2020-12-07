# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import ad_group_ad_asset_view_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_ad__group__ad__asset__view__pb2
from google.ads.google_ads.v6.proto.services import ad_group_ad_asset_view_service_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__ad__asset__view__service__pb2


class AdGroupAdAssetViewServiceStub(object):
    """Proto file describing the ad group ad asset view service.

    Service to fetch ad group ad asset views.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAdGroupAdAssetView = channel.unary_unary(
                '/google.ads.googleads.v6.services.AdGroupAdAssetViewService/GetAdGroupAdAssetView',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__ad__asset__view__service__pb2.GetAdGroupAdAssetViewRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_ad__group__ad__asset__view__pb2.AdGroupAdAssetView.FromString,
                )


class AdGroupAdAssetViewServiceServicer(object):
    """Proto file describing the ad group ad asset view service.

    Service to fetch ad group ad asset views.
    """

    def GetAdGroupAdAssetView(self, request, context):
        """Returns the requested ad group ad asset view in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdGroupAdAssetViewServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAdGroupAdAssetView': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAdGroupAdAssetView,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__ad__asset__view__service__pb2.GetAdGroupAdAssetViewRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_ad__group__ad__asset__view__pb2.AdGroupAdAssetView.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.AdGroupAdAssetViewService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdGroupAdAssetViewService(object):
    """Proto file describing the ad group ad asset view service.

    Service to fetch ad group ad asset views.
    """

    @staticmethod
    def GetAdGroupAdAssetView(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.AdGroupAdAssetViewService/GetAdGroupAdAssetView',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_ad__group__ad__asset__view__service__pb2.GetAdGroupAdAssetViewRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_ad__group__ad__asset__view__pb2.AdGroupAdAssetView.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)