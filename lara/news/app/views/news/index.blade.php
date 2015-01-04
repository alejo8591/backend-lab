@foreach($news as $item)
  <li>
    <a href="{{ route('news.show', $item->id)}}">
      {{$item->title}}
    </a>
  </li>
@endforeach
