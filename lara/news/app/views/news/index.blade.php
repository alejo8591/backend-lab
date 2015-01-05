{{ HTML::script('js/jquery-1.11.2.min.js') }}
{{ HTML::script('js/restfulizer.js') }}

<?php $status = Session::get('status'); ?>
@if($status == 'save')
<h3>La noticia se Guardo con exito</h3>
@endif

@if($status == 'delete')
<h3>La noticia se Elimino con exito</h3>
@endif


@foreach($news as $item)
  <li>
    <a href="{{ route('news.show', $item->id)}}">
      {{$item->title}}
    </a> -
    <a href="{{ route('news.destroy', $item->id)}}" data-method="delete" rel="nofollow" data-confirm="Esta Seguro de Eliminar el elemento">
      Eliminar
    </a>
    <!-- Basic form
    {{ Form::open(array('method' => 'DELETE', 'route' => array('news.destroy', $item->id))) }}
    {{ Form::submit('Eliminar', array('class'=>'button')) }}
    {{ Form::close() }} -->
  </li>
@endforeach
