from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

# Create your tests here.

class SnackTest(TestCase):
    def test_list_view_status(self):
        url = reverse('SnackListView')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_template(self):
        url = reverse('SnackListView')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'SnackListView.html')

    def setUp(self):

        self.user=get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='test')

        self.snack=Snack.objects.create(
            title='test',
            description="test",
            purchaser=self.user 
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack),'test')

    def test_detail_view(self):
        url = reverse('SnackDetailView',args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'SnackDetailView.html')

    def test_create_view(self):
        data={
            'title':'test',
            'description':"Test",
            'purchaser':self.user.id

         }
        url = reverse('SnackCreateView')
        response= self.client.post(path=url,data=data,follow=True)
        self.assertRedirects(response,reverse('SnackDetailView',args=[2]))