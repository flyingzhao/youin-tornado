class CreateUfiles < ActiveRecord::Migration
  def change
    create_table :ufiles do |t|
      t.string :filetype
      t.string :name
      t.string :filepath
      t.string :hashvalue
      t.timestamps null: false
    end
  end
end
