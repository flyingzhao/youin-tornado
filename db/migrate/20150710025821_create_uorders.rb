class CreateUorders < ActiveRecord::Migration
  def change
    create_table :uorders do |t|
      t.integer :user_id
      t.string :number
      t.string :state
      t.float :price
      
      t.timestamps null: false
    end
  end
end
