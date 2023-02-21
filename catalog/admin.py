from django.contrib import admin

from .models import Author, Genre, Book, BookInstance

# Este codigo importa los modelos y, a continuacion, llama para registrar cada uno de ellos.
# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)
# admin.site.register(BookInstance)


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name',
                    'date_of_birth', 'date_of_death')

    # enumera solo los campos que se mostrarán en el formulario, en orden.
    # Los campos se muestran verticalmente de forma predeterminada,
    # pero se mostrarán horizontalmente si los agrupa en una tupla (como se muestra en los campos de "fecha" arriba)
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    # también puede utilizar el excludeatributo para declarar una lista de atributos que se excluirán del formulario
    # (se mostrarán todos los demás atributos del modelo).

    inlines = [BooksInline]


# Register the admin class with the associated model
# Tambien se puede poner como  @admin.register(Author) encima de la definicion de la clase
admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Register the Admin classes for Book using the decorator


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # Hemos hecho una lista para que se vea mejor el libro
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')

    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
