from django.shortcuts import render
from .models import Comment
# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .serializers import CommentSerializer

# Create your views here.
class CommentDetailView(APIView):
    # GET single comment
    def get(self, request, pk):
        comment = Comment.objects.get(id=pk)
        serialized_comment = CommentSerializer(comment)
        return Response(serialized_comment.data, status=status.HTTP_200_OK)

    # EDIT comment
    def put(self, request, pk):
        comment = Comment.objects.get(id=pk) 
        updated_comment = CommentSerializer(comment, data=request.data)
        if updated_comment.is_valid():
            updated_comment.save()
            return Response(updated_comment.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(updated_comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    # DELETE comment
    def delete(self, request, pk):
        try:
            comment = Comment.objects.get(id=pk)
            comment.delete()
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentListView(APIView):
    # GET all comments
    def get(self,request):
        comments = Comment.objects.all()
        serialized_comments = CommentSerializer(comments, many=True)
        return Response(serialized_comments.data, status=status.HTTP_200_OK)

    # POST a comment
    def post(self,request):
        request.data['owners'] = request.user.id
        comment = CommentSerializer(data = request.data)
        if comment.is_valid():
            comment.save() 
            return Response(comment.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)