from odoo.exceptions import AccessError,UserError
from odoo.tests.common import TransactionCase
import logging

_logger = logging.getLogger(__name__)

class TestTodo(TransactionCase):

    def setUp(self, *args, **kwargs):
        super(TestTodo, self).setUp(*args, **kwargs)
        #Création d'un nouvel utilisateur pour les tests
        self.fresh_user = self.env['res.users'].create({
            'login': 'bob',
            'name': "Bob Bobman",
        })
        # Recherche de l'utilisateur avec les droits suffisants
        # sur le module
        self.task_manager = self.env.ref('todo_app.task_manager')

    def test_create(self):
        "Create a simple Todo"
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.is_done, False)
        self.assertEqual(task.active, True)
        self.assertEqual(task.date_deadline, False)
        self.assertEqual(task.user_id, self.env.ref('todo_app.task_manager'))
        self.assertEqual(len(task.team_ids), 1)

    def test_clear_done(self):
        "Clear Done sets to non active"
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        task.do_clear_done()
        self.assertFalse(task.active)

    def test_clear_done_exception(self):
        "Clear Done twice"
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        task.do_clear_done()
        with self.assertRaises(UserError):
            task.do_clear_done()

    def test_copy_once(self):
        "Copy a simple Todo"
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        copy = task.copy()
        self.assertEqual(copy.name, 'Copy of Test Task')

    def test_copy_twice(self):
        "Copy a simple Todo"
        Todo = self.env['todo.task'].with_user(self.task_manager)
        task = Todo.create({'name': 'Test Task'})
        first_copy = task.copy()
        second_copy = task.copy()
        self.assertEqual(first_copy.name, 'Copy of Test Task')
        self.assertEqual(second_copy.name, 'Copy of Test Task (1)')

    def test_record_rule(self):
        "Test for a user not in the group"
        Todo = self.env['todo.task'].with_user(self.fresh_user)
        with self.assertRaises(AccessError):
            task = Todo.create({'name': 'New Task'})