# Python Chat Uygulaması

Bu proje, Python kullanarak basit bir chat uygulaması oluşturmayı amaçlamaktadır. Flask ve Flask-SocketIO kütüphanelerini kullanarak canlı sohbet işlevselliği sağlayacaktır.

## Kurulum

1. Proje dosyalarınızı indirin veya klonlayın.

2. Gerekli Python paketlerini yükleyin:

3. `app.py` dosyasındaki `SECRET_KEY` değişkenini bir güvenlik anahtarı ile değiştirin.

## Kullanım

1. Python kodunu çalıştırın:

2. Tarayıcınızı açın ve `http://localhost:5000` adresine gidin.

3. Chat uygulamasına hoş geldiniz! Kullanıcı adınızı girin ve sohbet etmeye başlayın.

## Dışa Açık Erişim İçin ngrok Kullanımı

1. [Ngrok](https://ngrok.com) sitesine gidin ve ücretsiz bir hesap oluşturun.

2. Hesabınızı onayladıktan sonra, ngrok oturum açma bilgilerinizi kullanarak oturum açın.

3. Ngrok'un web arayüzüne erişin ve `AUTH TOKEN` bölümünde yer alan oturum açma bilgilerini `ngrok` komut satırında kullanmak için kullanın:

4. Dışa açık erişim sağlamak için ngrok'u çalıştırın. Örneğin, yerel sunucunuz 5000 portunda çalışıyorsa:


5. Çıktıda, ngrok tarafından sağlanan dışa açık erişim URL'sini bulacaksınız. Bu URL, sohbet uygulamanıza dünyanın herhangi bir yerinden erişim sağlar.

6. Artık ngrok URL'sini paylaşabilir ve başkalarının sohbet uygulamanıza erişmesine izin verebilirsiniz.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyin.

