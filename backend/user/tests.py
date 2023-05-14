from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class ViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # 예상 결과: 로그인 후 리다이렉트
        self.assertRedirects(response, reverse('home'))

    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # 예상 결과: 로그아웃 후 리다이렉트
        self.assertRedirects(response, reverse('home'))

    def test_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'newpassword',
            'password2': 'newpassword'
        })
        self.assertEqual(response.status_code, 302)  # 예상 결과: 회원 가입 후 리다이렉트
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())