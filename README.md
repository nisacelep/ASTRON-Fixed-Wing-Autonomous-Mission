


[Screencast from 11-23-2026 115017 AM.webm](https://github.com/user-attachments/assets/c2914484-9f34-48a9-809e-3a85b1831d72)

# ASTRON – PX4 ve MAVSDK ile Sabit Kanatlı İHA Otonom Görev Simülasyonu
## 1. Proje Hakkında

Bu proje, ASTRON Teknik Eğitim Programı kapsamında gerçekleştirilen İHA Yazılım ve Aviyonik Sistemler çalışmasının uygulama bölümüdür.

Projenin amacı, PX4 Autopilot kullanılarak sabit kanatlı bir İHA'nın simülasyon ortamında otonom görev gerçekleştirmesini incelemek ve bu süreci Python ile MAVSDK üzerinden yönetmektir.

Çalışmada PX4 SITL ve Gazebo simülasyon ortamı kullanılmıştır. QGroundControl üzerinden Bilecik çevresinde bir uçuş rotası oluşturulmuş ve bu rota üzerindeki waypoint noktaları kullanılarak uçuş simülasyonu gerçekleştirilmiştir.

Python ve MAVSDK kullanılarak PX4 ile haberleşme, görev başlatma ve telemetri verilerini takip etme işlemleri için bir uygulama hazırlanmıştır.

## 2. Projenin Amaçları

- PX4 Autopilot sisteminin çalışma mantığını öğrenmek.
- SITL simülasyon ortamını tanımak.
- Gazebo üzerinde sabit kanatlı İHA simülasyonu gerçekleştirmek.
- QGroundControl üzerinden uçuş rotası oluşturmak.
- Waypoint tabanlı otonom görev planlamasını incelemek.
- Python ve MAVSDK ile PX4 haberleşmesini sağlamak.
- Uçuş sırasında telemetri verilerini takip etmek.

## 3. Kullanılan Teknolojiler

| Teknoloji | Kullanım Amacı |
|---|---|
| Ubuntu | Geliştirme ve simülasyon işletim sistemi |
| PX4 Autopilot | İHA uçuş kontrol yazılımı |
| SITL | Uçuş kontrol yazılımının bilgisayar üzerinde simülasyonu |
| Gazebo | İHA'nın üç boyutlu simülasyon ortamı |
| QGroundControl | Uçuş rotası oluşturma ve görev yönetimi |
| MAVLink | Sistemler arası haberleşme protokolü |
| MAVSDK | Python üzerinden PX4 ile haberleşme kütüphanesi |
| Python | Görev yönetimi ve telemetri takibi |
| ROS 2 | Robotik sistemler için yazılım altyapısı |

## 4. Uygulama Aşamaları

1. Ubuntu ortamının hazırlanması.
2. PX4 SITL simülasyonunun başlatılması.
3. Gazebo ortamında sabit kanatlı İHA modelinin çalıştırılması.
4. QGroundControl bağlantısının gerçekleştirilmesi.
5. Bilecik çevresinde waypoint noktalarından oluşan uçuş rotasının hazırlanması.
6. Uçuş görevinin PX4'e yüklenmesi.
7. Python ve MAVSDK kullanılarak haberleşme uygulamasının hazırlanması.
8. Telemetri verilerinin takip edilmesi.
9. Simülasyon uçuşunun kaydedilmesi.

## 5. Python Uygulaması

Proje kapsamında `ucus.py` isimli bir Python dosyası hazırlanmıştır.

Uygulamanın temel işlevleri şunlardır:

- PX4 sistemine UDP üzerinden bağlanmak.
- İHA bağlantı durumunu kontrol etmek.
- Arm komutunu göndermek.
- Yüklenmiş mission görevini başlatmak.
- Mission ilerlemesini takip etmek.
- Konum, irtifa, hız ve uçuş durumunu okumak.
- Telemetri verilerini terminal ekranında görüntülemek.

## 6. Telemetri Takibi

Python uygulamasında MAVSDK Telemetry arayüzü kullanılarak aşağıdaki veriler takip edilmektedir:

- Enlem ve boylam
- Göreceli irtifa
- Yatay hız
- Havada olma durumu
- Uçuş modu
- Mission ilerleme durumu

## 7. Proje Çıktıları

Proje kapsamında aşağıdaki çıktılar sunulmaktadır:

- Python kaynak kodu
- Teorik teknik dokümantasyon
- Uygulama teknik raporu
- Bilecik uçuş rotası
- Sabit kanatlı İHA simülasyon uçuş videosu
- Telemetri çıktıları

## 8. Sonuç

Bu çalışma ile PX4 Autopilot ekosistemi, SITL simülasyonu, Gazebo ve QGroundControl kullanılarak sabit kanatlı İHA görev planlaması ve simülasyonu gerçekleştirilmiştir.

Python ve MAVSDK aracılığıyla uçuş kontrol sistemiyle haberleşme ve telemetri takibi konularında uygulama geliştirme deneyimi kazanılmıştır.

Proje, otonom İHA sistemlerinin yazılım altyapısını ve çalışma mantığını anlamaya yönelik uygulamalı bir çalışma niteliğindedir.
