from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from apps.api.models.client_model import Client
from apps.api.serializers import ClientSerializer


# view clients
@api_view(['GET', 'POST'])
def clients_list_view(request):
    """ shows all clients when method is get 
    or creates a new client if method is POST
    """
    # list clients
    if request.method == 'GET':
        clients = Client.objects.all()
        clients_serialized = ClientSerializer(clients, many=True)
        return Response(clients_serialized.data, status=status.HTTP_200_OK)

    # Create client
    if request.method == 'POST':
        client = ClientSerializer(data=request.data)
        if client.is_valid():
            client.save()
            return Response(client.data, status=status.HTTP_201_CREATED)
        return Response(client.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def clients_detail_view(request, id=None):
    """ shows a client by id when method is get,
    deletes a client by id if method is DELETE
    or updates a client by id if method is PUT
    """
    client = Client.objects.all().filter(id=id)
    if len(client) == 0:
        msg = 'Doesn´t exist an client with id={}'.format(id)
        return Response({'message': msg}, status=status.HTTP_404_NOT_FOUND)

    client = client.first()

    # retrive client
    if request.method == 'GET':

        client_serialized = ClientSerializer(client)
        return Response(client_serialized.data, status=status.HTTP_200_OK)

    # update client
    if request.method == 'PUT':
        edit_client = ClientSerializer(client, data=request.data)
        if edit_client.is_valid():
            edit_client.save()
            return Response(edit_client.data, status=status.HTTP_202_ACCEPTED)
        return Response(edit_client.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete client
    if request.method == 'DELETE':

        client.delete()
        msg = 'Client deleted successfully'
        return Response({'message': msg}, status=status.HTTP_200_OK)
