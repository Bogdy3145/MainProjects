import android.os.Parcel
import android.os.Parcelable

data class Service(
    val id: Long,  // Unique ID for each service
    val name: String,
    val provider: String,
    val location: String,
    val radius: Int,
    val phone: String,
    val price: Int,
    //val imageResId: Int
) : Parcelable {
    constructor(parcel: Parcel) : this(
        parcel.readLong(),
        parcel.readString() ?: "",
        parcel.readString() ?: "",
        parcel.readString() ?: "",
        parcel.readInt(),
        parcel.readString() ?: "",
        parcel.readInt(),
        //parcel.readInt()
    )

    override fun writeToParcel(parcel: Parcel, flags: Int) {
        parcel.writeLong(id)
        parcel.writeString(name)
        parcel.writeString(provider)
        parcel.writeString(location)
        parcel.writeInt(radius)
        parcel.writeString(phone)
        parcel.writeInt(price)
        //parcel.writeInt(imageResId)
    }

    override fun describeContents(): Int {
        return 0
    }

    companion object CREATOR : Parcelable.Creator<Service> {
        override fun createFromParcel(parcel: Parcel): Service {
            return Service(parcel)
        }

        override fun newArray(size: Int): Array<Service?> {
            return arrayOfNulls(size)
        }
    }
}
