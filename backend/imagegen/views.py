from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class GenerateImageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        prompt = request.data.get("prompt")

        # Burada AI image generation logic olacak
        generated_image_url = f"https://example.com/generated/{user.id}.png"

        return Response({
            "user": user.email,
            "prompt": prompt,
            "image_url": generated_image_url
        })
