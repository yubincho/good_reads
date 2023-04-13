
## 해외 GoodReads Clone 
title : Good Readers  
( http://mybookmanage.com/으로 서버에 올렸으나 1년 후 서버 구동을 중지하였습니다. )
( 해외 GoodReads를 참고하여 만듦. )  
  
* 언어 : 파이썬 ( python version = 3.8 )
* 프레임워크 : Django ( django version = 3.1 ) 
* 가상환경 = pipenv 이용.  
     
----------------------------------------------------------------- 
   
1. 기능 
* 게시판 검색기능.
* django-allauth - 구글 로그인 연동, 로그인, 회원가입 기능.
* 회원 탈퇴 - 개인 프로젝트이므로, 회원 탈퇴시 모든 정보 삭제 기능.
* 내 목록 추가/삭제 기능 - 쇼핑몰의 장바구니 기능 응용.
* ListView/DetailView & function base view를 혼합하여 사용.
* 기타 : 댓글 기능, 평점 기능  
-------------------------------------------------------------------
   
2. sublibrary 설치 방법 예
* pipenv install django-allauth 
* pipenv install django-crispy-forms
+ INSTALLED_APPS = ["django.contrib.sites", 
    "crispy_forms", ] 
+ SITE_ID = 1 
+ python manage.py migrate  
 
-------------------------------------------------------------------- 

3. 배포 
* https://my.vultr.com/ 이용.
  
        
 
  
