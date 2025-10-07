# 1. Projeyi klonla
git clone [repo-url] <br>
cd mycreatool

# 2. Docker Kur

# 3. Docker'ı Çalıştır
Ana proje klasöründeyken (/mycreatool):
<br> docker-compose build <br>
docker-compose up -d

# 4. Erişim adresleri
### Frontend: http://localhost:5173
### Backend: http://localhost:8000
### Admin: http://localhost:8000/admin/

#### Admin arayüzüne girerken gireceğin e-posta ve şifre:
nuriakkurt@mycreatool.com
Mycreatool1234

# 5. Yapay Zeka
İlk önce fotoğraf ekleme yapılacak: <br>
-Hangi dilde yazılırsa yazılsın, prompta göre en doğru sonuçları vermesi gerek.
Bu noktada belki prompt iyileştirme yapılabilir. Ancak bu eğer ekstra maliyet üretirse
 bize uygun olmaz.
Ardından fotoğraf düzenleme. Bu sonradan geliştirilebilir.
backend/imagegen klasörü bunun için oluşturulmuştur. image işlemleri için kullanılacak app'tir.
Webhook mantığı kullanılmalı. 