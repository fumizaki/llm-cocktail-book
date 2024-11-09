import { auth } from "@/auth/config";

export const getAccessToken = async () => {
    const session = await auth()
    return session?.user.authorization.access_token
}