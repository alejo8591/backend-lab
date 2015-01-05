<?php

class NewsController extends \BaseController {

	/**
	 * Display a listing of the resource.
	 * GET /news
	 *
	 * @return Response
	 */
	public function index()
	{
		$news = News::all();

		return View::make('news.index', compact('news'));
	}

	/**
	 * Show the form for creating a new resource.
	 * GET /news/create
	 *
	 * @return Response
	 */
	public function create()
	{
		return View::make('news.create');
	}

	/**
	 * Store a newly created resource in storage.
	 * POST /news
	 *
	 * @return Response
	 */
	public function store()
	{
		// MVC
		$news = new News;

		$news->title = Input::get('title');
		$news->content = Input::get('content');
		$news->active = Input::get('active');

		$news->save();

		// Normal
		/*DB::table('news')->insert(array(
			'title' => Input::get('title'),
			'content' => Input::get('content'),
			'active' => Input::get('active'),
		));*/

		return Redirect::to('news')->with('status', 'save');
	}

	/**
	 * Display the specified resource.
	 * GET /news/{id}
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function show($id)
	{
		$news = News::find($id);

		return View::make('news.show', compact('news'));
	}

	/**
	 * Show the form for editing the specified resource.
	 * GET /news/{id}/edit
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function edit($id)
	{
		//
	}

	/**
	 * Update the specified resource in storage.
	 * PUT /news/{id}
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function update($id)
	{
		//
	}

	/**
	 * Remove the specified resource from storage.
	 * DELETE /news/{id}
	 *
	 * @param  int  $id
	 * @return Response
	 */
	public function destroy($id)
	{
		$news = News::find($id);

		$news->delete();

		//return "La Noticia fue Eliminada";
		// Other 	`whith` method
		//return Redirect::to('news')->withDelete('ok');
		return Redirect::to('news')->with('status','delete');

	}

}
