from todo_app.data.view_model import ViewModel
from todo_app.data.item import Item

def test_view_model_todo_items_property_only_shows_todo_status_items():
    # Given
    test_items = [
        Item("123", "To Do Item", "To Do"),
        Item("345", "Complete Item", "Done")
    ]

    test_view_model = ViewModel(test_items)

    # When
    returned_items = test_view_model.todo_items

    # Then
    assert len(returned_items) == 1