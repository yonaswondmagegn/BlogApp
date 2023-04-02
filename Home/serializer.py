from rest_framework import serializers
from Profile.serializer import ProfileSerializer
from .models import (Blog,BlogComment,
                     BlogImageFragment,
                     BlogVideoFragment
                     )


    
class BlogImageFragmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogImageFragment
        fields = "__all__"

class BlogVideoFragmentSerializer(serializers.ModelSerializer):
        class Meta:
            model = BlogVideoFragment
            fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
         images = BlogImageFragmentSerializer(many = True)
         videos = BlogVideoFragmentSerializer(many = True)
         number_of_likes = serializers.SerializerMethodField(method_name="like_count")
         number_of_comment = serializers.SerializerMethodField(method_name="comment_count")


         class Meta:
            model = Blog
            fields = "__all__"

            
         
         def like_count(self,obj):
              return obj.likes.count()
         
         def comment_count(self,obj):
              return BlogComment.objects.filter(blog = obj).count()
         
         def create(self, validated_data):
               blog_videofragment_data = validated_data.pop('video_fragments',[])
               blog_imagefragment_data = validated_data.pop('images_fragments',[])
               blog = Blog.objects.create(**validated_data)

               for fragment in blog_videofragment_data:
                    video_fragment = BlogVideoFragment.objects.create(**fragment)
                    blog.videos.add(video_fragment)
                    
               for fragment in blog_imagefragment_data:
                    image_fragment = BlogImageFragment.objects.create(**fragment)
                    blog.images.add(image_fragment)
               return blog


class BlogCommentSerializer(serializers.ModelSerializer):
     user = serializers.SerializerMethodField(method_name="get_commenter")
     replay_for = serializers.SerializerMethodField(method_name="get_replay_for")
     likes = serializers.SerializerMethodField(method_name="like_count")

     class Meta:
          model = BlogComment
          fields = ['id','user',
                    'blog','type',
                    'replay_for',
                    'text','likes','date']

     def get_commenter(self,obj):
          return ProfileSerializer(obj.user.profile).data
     
     def get_replay_for(self,obj):
          if (obj.type == 'R'):
               return BlogCommentSerializer(obj.replay_for).data
          else:
               return ''
     
     def like_count(self,obj):
          return obj.likes.count()
     
     
               
                 


     

