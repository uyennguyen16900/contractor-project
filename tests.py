from unittest import TestCase, main as unittest_main, mock
from app import app
from bson.objectid import ObjectId

sample_drink_id = ObjectId('5d55cffc4a3d4021f42827a3')
sample_drink = {
    'name': 'Jasmine Green Milk Tea',
    'price': '5',
    'description': 'Jasmine green tea, boba, honey, milk',
    'images': ['https://fubellyhouston.com/wp-content/uploads/2017/04/original-138-720x720.jpeg']
}
sample_form_data = {
    'name': sample_drink['name'],
    'price': sample_drink['price'],
    'description': sample_drink['description'],
    'images': sample_drink['images']
}

class DrinksTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    # def test_index(self):
    #     """Test the drinks homepage."""
    #     result = self.client.get('/')
    #     self.assertEqual(result.status, '200 OK')
    #     self.assertIn(b'Drink', result.data)

    def test_new(self):
        """Test the new drink creation page."""
        result = self.client.get('drinks/new')
        self.assertEqual(result.status, '200 OK')
        self.assertIn(b'New Drink',result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_drink(self, mock_find):
        """Test showing a single drink."""
        mock_find.return_value = sample_drink

        result = self.client.get(f'/drinks/{sample_drink_id}')
        self.assertEqual(result.status, '200 OK')
        # self.assertIn(b'Cat Videos', result.data)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_edit_drink(self, mock_find):
        """Test editing a single drink."""
        mock_find.return_value = sample_drink

        result = self.client.get(f'/drinks/{sample_drink_id}/edit')
        self.assertEqual(result.status, '200 OK')
        # self.assertIn(b'Cat Videos', result.data)

    # @mock.patch('pymongo.collection.Collection.insert_one')
    # def test_submit_drink(self, mock_insert):
    #     """Test submitting a new drink."""
    #     result = self.client.post('/drinks', data=sample_form_data)
    #
    #     # After submitting, should redirect to that drink's page
    #     self.assertEqual(result.status, '302 FOUND')
    #     mock_insert.assert_called_with(sample_drink)

    # @mock.patch('pymongo.collection.Collection.update_one')
    # def test_update_drink(self, mock_update):
    #     result = self.client.post(f'/drinks/{sample_drink_id}', data=sample_form_data)
    #
    #     self.assertEqual(result.status, '302 FOUND')
    #     mock_update.assert_called_with({'_id': sample_drink_id}, {'$set': sample_drink})

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_delete_drink(self, mock_delete):
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/drinks/{sample_drink_id}/delete', data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_drink_id})

if __name__ == '__main__':
    unittest_main()
