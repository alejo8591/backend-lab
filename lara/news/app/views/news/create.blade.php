{{ Form::open() }}
  {{ Form::label('title', 'Titulo de la Noticia') }}: {{ Form::text('title') }} <br />
  {{ Form::label('content', 'Contenido de noticia') }}:  {{ Form::textarea('content') }} <br />
  {{ Form::label('active', 'Publicar') }}:  {{ Form::text('active') }} <br />

  {{ Form::submit('Crear Noticia') }}

{{ Form::close() }}
