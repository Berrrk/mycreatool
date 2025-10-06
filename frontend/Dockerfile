# Temel imaj
FROM node:alpine
LABEL authors="berkzengin"

# Çalışma dizini
WORKDIR /app

# package.json dosyasını kopyala
COPY package*.json ./

# Bağımlılıkları npm ile kur (dev dependencies dahil)
RUN npm install --include=dev

# Uygulama kodunun geri kalanını kopyala
COPY . .

# Port'u aç
EXPOSE 5173

# Uygulamayı yarn ile çalıştır
CMD ["npm", "run", "dev"]